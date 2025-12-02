# __init__ (function)

**Code:**
```python
def __init__(self):
        self.rate_limit_storage: Dict[str, List[datetime]] = {}
        self.session = requests.Session()
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        self.session.verify = True
```

**Explanation:**
**What this `__init__` does (in plain English)**  

When a new `URLDownloader` object is created it:

1. **Prepares a place to remember recent requests**  
   - `self.rate_limit_storage` is an empty dictionary that will later hold, for each domain, a list of timestamps of the last few downloads. This is used to enforce a per‑domain rate limit.

2. **Sets up a reusable HTTP client**  
   - `self.session = requests.Session()` creates a single `requests` session that will be reused for all downloads, which is faster and keeps cookies/headers across calls.

3. **Adds retry logic for HTTPS**  
   - `self.session.mount('https://', HTTPAdapter(max_retries=3))` tells the session to automatically retry up to 3 times on transient network errors when talking to HTTPS URLs.

4. **Enforces SSL verification**  
   - `self.session.verify = True` ensures that every HTTPS request will validate the server’s SSL certificate (the default, but set explicitly for clarity).

In short, the constructor builds a ready‑to‑use HTTP client with retry support and a structure for tracking how many requests have been made to each domain.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
