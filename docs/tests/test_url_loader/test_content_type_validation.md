# test_content_type_validation (function)

**Code:**
```python
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
```

**Explanation:**
**Function Explanation: `test_content_type_validation`**

This function tests the content type validation of the `downloader` class. It checks if the `downloader` raises a `BadRequestError` when trying to download a file with an unsupported content type.

Here's a step-by-step breakdown:

1. It defines a list of invalid content types (`invalid_types`).
2. It loops through each invalid content type.
3. For each content type, it creates a mock response with the invalid content type.
4. It patches the `requests.Session.get` function to return the mock response.
5. It calls the `downloader.download` method with a URL that has the invalid content type.
6. It expects the `downloader` to raise a `BadRequestError` with a message containing "Unsupported file type".

In simple terms, this function ensures that the `downloader` class correctly handles files with unsupported content types by raising a `BadRequestError` with a meaningful error message.

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
