# _validate_content_type (function)

**Code:**
```python
def _validate_content_type(self, url: str, content_type: str) -> FileType:
        try:
            content_type = content_type.split(';')[0].lower()

            if content_type in MIME_TO_FILE_TYPE:
                return MIME_TO_FILE_TYPE[content_type]

            ext = Path(urllib.parse.urlparse(url).path).suffix.lower()
            if ext in EXT_TO_FILE_TYPE:
                return EXT_TO_FILE_TYPE[ext]

            raise BadRequestError(f"Unsupported file type: {content_type}")
        except BadRequestError:
            raise
        except Exception as e:
            raise BadRequestError(f"Error validating content type: {str(e)}")
```

**Explanation:**
**What it does**

`_validate_content_type` decides what kind of file we’re downloading.

1. **Normalize the MIME header** – it strips any parameters (`; charset=utf‑8`) and lower‑cases it.  
2. **Look up the MIME** – if the MIME is in the `MIME_TO_FILE_TYPE` map, return the corresponding `FileType`.  
3. **Fall back to the URL extension** – if the MIME isn’t known, extract the file extension from the URL and look it up in `EXT_TO_FILE_TYPE`.  
4. **Error if unknown** – if neither lookup works, raise `BadRequestError` (“Unsupported file type”).  
5. **Catch any other exception** – wrap it in a `BadRequestError` with a helpful message.

**Why it matters**

- Keeps the downloader strict about what it accepts.  
- Allows the caller to know the exact `FileType` (pdf, xlsx, txt, etc.) for further processing.  
- Provides clear, consistent error handling for unsupported or malformed content types.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
