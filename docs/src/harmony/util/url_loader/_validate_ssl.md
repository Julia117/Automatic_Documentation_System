# _validate_ssl (function)

**Code:**
```python
def _validate_ssl(self, response: requests.Response) -> None:
        cert = response.raw.connection.sock.getpeercert()
        if not cert:
            raise ForbiddenError("Invalid SSL certificate")

        not_after = ssl.cert_time_to_seconds(cert['notAfter'])
        if datetime.fromtimestamp(not_after) < datetime.now():
            raise ForbiddenError("Expired SSL certificate")
```

**Explanation:**
**What `_validate_ssl` does**

```python
def _validate_ssl(self, response: requests.Response) -> None:
    cert = response.raw.connection.sock.getpeercert()
    if not cert:
        raise ForbiddenError("Invalid SSL certificate")

    not_after = ssl.cert_time_to_seconds(cert['notAfter'])
    if datetime.fromtimestamp(not_after) < datetime.now():
        raise ForbiddenError("Expired SSL certificate")
```

1. **Pull the server’s SSL certificate**  
   `response.raw.connection.sock.getpeercert()` grabs the certificate that the server presented during the HTTPS handshake.

2. **Check that a certificate was actually received**  
   If `cert` is `None` or empty, the connection didn’t provide a valid certificate → raise `ForbiddenError`.

3. **Check the certificate’s expiry date**  
   * `cert['notAfter']` is the expiry string (e.g., `"Jan 1 00:00:00 2020 GMT"`).  
   * `ssl.cert_time_to_seconds` converts that string to a Unix timestamp.  
   * `datetime.fromtimestamp(not_after)` turns the timestamp into a `datetime` object.  
   * If that date is in the past (`< datetime.now()`), the certificate is expired → raise `ForbiddenError`.

**Bottom line:**  
The function ensures the HTTPS response came with a valid, non‑expired SSL certificate; otherwise it blocks the download by throwing a `ForbiddenError`.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
