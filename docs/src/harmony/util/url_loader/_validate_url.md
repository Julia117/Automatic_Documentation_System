# _validate_url (function)

**Code:**
```python
def _validate_url(self, url: str) -> None:
        try:
            parsed = urllib.parse.urlparse(url)

            if parsed.scheme not in ALLOWED_SCHEMES:
                raise BadRequestError(f"URL must use HTTPS")

            if not parsed.netloc or '.' not in parsed.netloc:
                raise BadRequestError("Invalid domain")

            if '..' in parsed.path or '//' in parsed.path:
                raise ForbiddenError("Path traversal detected")

            if parsed.fragment:
                raise BadRequestError("URL fragments not supported")

            blocked_domains = {'localhost', '127.0.0.1', '0.0.0.0'}
            if parsed.netloc in blocked_domains:
                raise ForbiddenError("Access to internal domains blocked")

        except Exception as e:
            raise BadRequestError(f"Invalid URL: {str(e)}")
```

**Explanation:**
**What `_validate_url` does (in plain English)**  

1. **Parse the URL** – Uses `urllib.parse.urlparse` to split the string into parts (scheme, netloc, path, fragment, …).  

2. **Check the scheme** – Only HTTPS is allowed. If the scheme is anything else (e.g., `http`, `ftp`) it raises a `BadRequestError`.  

3. **Validate the domain** –  
   * The host part (`netloc`) must exist and contain a dot (`.`).  
   * If it’s missing or malformed, a `BadRequestError` is raised.  

4. **Guard against path traversal** –  
   * If the path contains `..` or `//`, it could be trying to escape the intended directory.  
   * In that case a `ForbiddenError` is raised.  

5. **Disallow fragments** – URLs that end with `#something` are rejected with a `BadRequestError`.  

6. **Block internal addresses** – `localhost`, `127.0.0.1`, and `0.0.0.0` are considered internal and are forbidden; a `ForbiddenError` is raised.  

7. **Error handling** – Any exception that slips through the checks is caught and re‑raised as a `BadRequestError` with a helpful message.  

In short, the function ensures the URL is a safe, well‑formed HTTPS link that points to an external domain and doesn’t contain suspicious path or fragment components before the downloader proceeds.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
