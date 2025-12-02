# TestURLLoader (class)

**Code:**
```python
class TestURLLoader(unittest.TestCase):
    def setUp(self):
        self.downloader = URLDownloader()
        self.valid_url = "https://example.com/test.pdf"

        self.downloader.rate_limit_storage.clear()

        self.mock_response = MagicMock()
        self.mock_response.headers = {
            'content-type': 'application/pdf',
            'content-length': '1000'
        }
        self.mock_response.content = b'test content'
        self.mock_response.raw = MagicMock()
        self.mock_response.raw.connection = MagicMock()
        self.mock_response.raw.connection.sock = MagicMock()
        self.mock_response.raw.connection.sock.getpeercert.return_value = {
            'notAfter': 'Dec 31 23:59:59 2125 GMT'
        }

        def mock_iter_content(chunk_size=None):
            yield b'test content'

        self.mock_response.iter_content = mock_iter_content

    def test_content_integrity(self):
        with patch('requests.Session.get', return_value=self.mock_response):
            raw_file = self.downloader.download(self.valid_url)
            self.assertIsNotNone(raw_file.metadata)
            self.assertIn('content_hash', raw_file.metadata)
            expected_hash = '6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72'
            self.assertEqual(raw_file.metadata['content_hash'], expected_hash)

    def test_content_type_validation(self):
        invalid_types = [
            "application/javascript",
            "application/x-executable",
            "application/octet-stream"
        ]

        for content_type in invalid_types:
            with self.subTest(content_type=content_type):
                mock_response = MagicMock()
                mock_response.headers = {
                    'content-type': content_type,
                }
                mock_response.raw = self.mock_response.raw
                mock_response.iter_content = self.mock_response.iter_content
                mock_response.raise_for_status = lambda: None

                with patch('requests.Session.get', return_value=mock_response):
                    with self.assertRaises(BadRequestError) as cm:
                        self.downloader.download("https://example.com/test.unknown")
                    self.assertIn("Unsupported file type", str(cm.exception))

    def test_file_size_limit(self):
        mock_response = MagicMock()
        mock_response.headers = {
            'content-type': 'application/pdf',
            'content-length': str(MAX_FILE_SIZE + 1)
        }
        mock_response.raw = self.mock_response.raw
        mock_response.iter_content = self.mock_response.iter_content

        with patch('requests.Session.get', return_value=mock_response):
            with self.assertRaises(ForbiddenError):
                self.downloader.download(self.valid_url)

    def test_file_types(self):
        test_files = {
            'test.pdf': (FileType.pdf, 'application/pdf'),
            'test.xlsx': (FileType.xlsx, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            'test.txt': (FileType.txt, 'text/plain'),
            'test.csv': (FileType.csv, 'text/csv'),
            'test.docx': (FileType.docx, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        }

        for filename, (file_type, mime_type) in test_files.items():
            with self.subTest(file_type=file_type):
                url = f"https://example.com/{filename}"
                mock_response = MagicMock()
                mock_response.headers = {
                    'content-type': mime_type,
                    'content-length': '1000'
                }
                mock_response.raw = self.mock_response.raw
                mock_response.content = b'test content'
                mock_response.iter_content = lambda chunk_size: [b'test content']

                with patch('requests.Session.get', return_value=mock_response):
                    raw_file = self.downloader.download(url)
                    self.assertEqual(raw_file.file_type, file_type)

    def test_rate_limiting(self):
        self.downloader.rate_limit_storage.clear()

        with patch('requests.Session.get', return_value=self.mock_response):
            # initial request
            self.downloader.download(self.valid_url)

            # block after too many requests
            self.downloader.rate_limit_storage['example.com'] = [
                datetime.now() for _ in range(RATE_LIMIT_REQUESTS)
            ]

            with self.assertRaises(ConflictError):
                self.downloader.download(self.valid_url)

    def test_successful_instrument_loading(self):
        self.downloader.rate_limit_storage.clear()

        self.mock_response.iter_content = lambda chunk_size: [b'test content']

        with patch('requests.Session.get', return_value=self.mock_response):
            instruments = load_instruments_from_url(self.valid_url)
            self.assertIsInstance(instruments, list)

    def test_error_handling(self):
        error_conditions = {
            requests.Timeout: SomethingWrongError,
            requests.TooManyRedirects: ForbiddenError,
            requests.ConnectionError: SomethingWrongError
        }

        for exception, expected_error in error_conditions.items():
            with self.subTest(error=exception.__name__):
                with patch('requests.Session.get', side_effect=exception()):
                    with self.assertRaises(expected_error):
                        self.downloader.download(self.valid_url)

    def test_http_error_handling(self):
        error_codes = {
            401: ForbiddenError,  # unauthorized
            403: ForbiddenError,  # forbidden
            429: ConflictError,  # rate limit
            500: SomethingWrongError,  # server error
        }

        for status_code, expected_error in error_codes.items():
            with self.subTest(status_code=status_code):
                mock_response = MagicMock()
                mock_response.raise_for_status.side_effect = requests.RequestException(
                    response=MagicMock(status_code=status_code)
                )

                with patch('requests.Session.get', return_value=mock_response):
                    with self.assertRaises(expected_error):
                        self.downloader.download(self.valid_url)

    def test_ssl_validation(self):
        mock_response = MagicMock()
        mock_response.headers = self.mock_response.headers
        mock_response.content = self.mock_response.content
        mock_response.iter_content = self.mock_response.iter_content
        mock_response.raw = MagicMock()
        mock_response.raw.connection = MagicMock()
        mock_response.raw.connection.sock = MagicMock()
        mock_response.raw.connection.sock.getpeercert.return_value = {
            'notAfter': 'Jan 1 00:00:00 2020 GMT'
        }

        with patch('requests.Session.get', return_value=mock_response):
            with self.assertRaises(ForbiddenError):
                self.downloader.download(self.valid_url)

    def test_url_validation(self):
        invalid_urls = [
            "not-a-url",
            "http://example.com",  # HTTP not allowed
            "https://localhost",
            "https://127.0.0.1",
            "https://example.com/../test.pdf",  # path traversing
            "https://example.com/test.pdf#fragment"
        ]

        for url in invalid_urls:
            with self.subTest(url=url):
                with self.assertRaises((BadRequestError, ForbiddenError)):
                    self.downloader.download(url)
```

**Explanation:**
**Class Explanation: `TestURLLoader`**

The `TestURLLoader` class is a unit test case for the `URLDownloader` class. It contains a series of test methods that verify the functionality of the `URLDownloader` class.

**Key Features:**

1. **Mocking**: The class uses mocking to isolate the dependencies of the `URLDownloader` class, making it easier to test its behavior.
2. **Test Cases**: The class contains multiple test cases that cover various scenarios, such as:
	* Content integrity
	* Content type validation
	* File size limit
	* File types
	* Rate limiting
	* Successful instrument loading
	* Error handling
	* HTTP error handling
	* SSL validation
	* URL validation
3. **Assertions**: Each test case includes assertions to verify that the `URLDownloader` class behaves as expected.

**Purpose:**

The `TestURLLoader` class is designed to ensure that the `URLDownloader` class is working correctly and handles various edge cases. By running these tests, developers can have confidence that the `URLDownloader` class is reliable and efficient.

**Example Use Case:**

To use the `TestURLLoader` class, simply run the tests using a testing framework like Pytest or Unittest. This will execute all the test cases and report any failures or errors.

**Imports:**
```
import requests, import sys, import unittest, from datetime import datetime, from unittest.mock import patch, MagicMock, from harmony.util.url_loader import (
    URLDownloader,
    load_instruments_from_url,
    MAX_FILE_SIZE,
    RATE_LIMIT_REQUESTS
), from harmony.schemas.errors.base import (
    BadRequestError,
    ForbiddenError,
    ConflictError,
    SomethingWrongError
), from harmony.schemas.requests.text import FileType
```
