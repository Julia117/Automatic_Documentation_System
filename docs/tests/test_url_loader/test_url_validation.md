# test_url_validation (function)

**Code:**
```python
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
**Function Explanation: `test_url_validation`**

This function tests the URL validation functionality of the `URLDownloader` class. It checks if the `download` method raises the correct errors when given invalid URLs.

Here's a step-by-step breakdown:

1. A list of invalid URLs is defined.
2. The function iterates over each URL in the list.
3. For each URL, it uses the `subTest` context manager to identify the specific URL being tested.
4. It then attempts to download the URL using the `download` method of the `URLDownloader` class.
5. The function expects the `download` method to raise either a `BadRequestError` or a `ForbiddenError` when given an invalid URL.

In simple terms, this function ensures that the `URLDownloader` class correctly validates URLs and raises the expected errors when given invalid input.

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
