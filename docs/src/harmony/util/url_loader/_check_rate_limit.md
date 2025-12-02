# _check_rate_limit (function)

**Code:**
```python
def _check_rate_limit(self, domain: str) -> None:
        now = datetime.now()
        if domain not in self.rate_limit_storage:
            self.rate_limit_storage[domain] = []

        self.rate_limit_storage[domain] = [
            ts for ts in self.rate_limit_storage[domain]
            if ts > now - timedelta(seconds=RATE_LIMIT_WINDOW)
        ]

        if len(self.rate_limit_storage[domain]) >= RATE_LIMIT_REQUESTS:
            raise ConflictError("Rate limit exceeded")

        self.rate_limit_storage[domain].append(now)
```

**Explanation:**
**What it does**

`_check_rate_limit` keeps a per‑domain history of the timestamps of the last few requests.  
When a new request comes in:

1. **Clean old entries** – remove any timestamps older than the configured window (`RATE_LIMIT_WINDOW` seconds).  
2. **Check the count** – if the number of remaining timestamps is already at or above the allowed maximum (`RATE_LIMIT_REQUESTS`), raise a `ConflictError` (“Rate limit exceeded”).  
3. **Record the new request** – append the current time to the list for that domain.

**Why it matters**

This prevents a client from hammering a single domain too quickly. Each domain gets its own counter, and the counter is automatically reset as old requests fall outside the time window. If the limit is hit, the caller receives a clear error that can be handled or retried later.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
