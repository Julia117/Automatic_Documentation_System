# _check_legal_headers (function)

**Code:**
```python
def _check_legal_headers(self, response: requests.Response) -> None:
        if response.headers.get('X-Robots-Tag', '').lower() == 'noindex':
            raise ForbiddenError("Access not allowed by robots directive")

        if 'X-Copyright' in response.headers:
            raise ForbiddenError("Content is copyright protected")

        if 'X-Terms-Of-Service' in response.headers:
            raise ForbiddenError("Terms of service acceptance required")
```

**Explanation:**
**What `_check_legal_headers` does**

When the downloader receives an HTTP response it looks at three custom headers that a server can send to tell the client how the content may be used:

| Header | What it means | What the function does |
|--------|---------------|------------------------|
| `X-Robots-Tag` | Instructs crawlers/search‑engines. If the value is `noindex` the site says “don’t index or use this page.” | If the header is present and equals `noindex` (case‑insensitive), the function raises a `ForbiddenError` – the downloader stops and reports “Access not allowed by robots directive.” |
| `X-Copyright` | Indicates the content is protected by copyright. | If this header exists, a `ForbiddenError` is raised with the message “Content is copyright protected.” |
| `X-Terms-Of-Service` | Signals that the user must accept terms of service before using the content. | If this header is present, a `ForbiddenError` is raised with “Terms of service acceptance required.” |

**Bottom line**

The function enforces simple “do‑not‑use” rules that a server can signal via these headers. If any of them are present, the download is aborted by throwing a `ForbiddenError`. This keeps the downloader compliant with the server’s usage policies.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
