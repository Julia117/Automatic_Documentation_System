# download (function)

**Code:**
```python
def download(self, url: str) -> RawFile:
        try:
            self._validate_url(url)
            domain = urllib.parse.urlparse(url).netloc
            self._check_rate_limit(domain)

            response = self.session.get(
                url,
                timeout=DOWNLOAD_TIMEOUT,
                stream=True,
                verify=True,
                allow_redirects=True,
                headers={
                    'User-Agent': 'HarmonyBot/1.0 (+https://harmonydata.ac.uk)',
                    'Accept': ', '.join(MIME_TO_FILE_TYPE.keys())
                }
            )
            response.raise_for_status()

            self._validate_ssl(response)
            self._check_legal_headers(response)

            content_length = response.headers.get('content-length')
            if content_length and int(content_length) > MAX_FILE_SIZE:
                raise ForbiddenError(f"File too large: {content_length} bytes (max {MAX_FILE_SIZE})")

            file_type = self._validate_content_type(url, response.headers.get('content-type', ''))

            hasher = hashlib.sha256()
            content = b''
            for chunk in response.iter_content(chunk_size=8192):
                hasher.update(chunk)
                content += chunk

            if file_type in [FileType.pdf, FileType.xlsx, FileType.docx]:
                content_str = f"data:{response.headers['content-type']};base64," + base64.b64encode(content).decode(
                    'ascii')
            else:
                content_str = content.decode('utf-8')

            return RawFile(
                file_id=str(uuid.uuid4()),
                file_name=Path(urllib.parse.urlparse(url).path).name or "downloaded_file",
                file_type=file_type,
                content=content_str,
                metadata={
                    'content_hash': hasher.hexdigest(),
                    'download_timestamp': datetime.now().isoformat(),
                    'source_url': url
                }
            )

        except (BadRequestError, ForbiddenError, ConflictError):
            raise
        except requests.Timeout:
            raise SomethingWrongError("Download timeout")
        except requests.TooManyRedirects:
            raise ForbiddenError("Too many redirects")
        except requests.RequestException as e:
            if e.response is not None:
                if e.response.status_code == 401:
                    raise ForbiddenError("Resource requires authentication")
                elif e.response.status_code == 403:
                    raise ForbiddenError("Access forbidden")
                elif e.response.status_code == 429:
                    raise ConflictError("Rate limit exceeded")
            raise SomethingWrongError(f"Download error: {str(e)}")
        except Exception as e:
            raise SomethingWrongError(f"Unexpected error: {str(e)}")
```

**Explanation:**
**What the `download` method does (in plain English)**  

1. **Validate the URL** – checks scheme, domain, path safety, and blocks internal hosts.  
2. **Rate‑limit** – keeps a per‑domain counter and refuses the request if the limit is hit.  
3. **HTTP GET** – uses a persistent `requests.Session` with a custom User‑Agent and a list of accepted MIME types.  
4. **Check response** –  
   * `raise_for_status()` ensures a 2xx status.  
   * SSL certificate is verified and not expired.  
   * Certain headers (`X‑Robots‑Tag`, `X‑Copyright`, `X‑Terms‑Of‑Service`) are checked for legal restrictions.  
   * The `Content‑Length` header is compared to `MAX_FILE_SIZE`; too large → `ForbiddenError`.  
5. **Determine file type** – from the `Content‑Type` header or the URL extension.  
6. **Read the body in 8 KB chunks** –  
   * Updates a SHA‑256 hash for integrity.  
   * Builds the full byte payload.  
7. **Encode the payload** –  
   * Binary files (`pdf`, `xlsx`, `docx`) are base64‑encoded and prefixed with a data URI.  
   * Text files are decoded as UTF‑8.  
8. **Return a `RawFile`** – a dataclass containing:  
   * a new UUID,  
   * the original file name (or “downloaded_file”),  
   * the detected file type,  
   * the encoded content,  
   * metadata: hash, timestamp, and source URL.  

**Error handling**  
* Known custom errors (`BadRequestError`, `ForbiddenError`, `ConflictError`) are re‑raised.  
* `requests.Timeout` → `SomethingWrongError("Download timeout")`.  
* `requests.TooManyRedirects` → `ForbiddenError`.  
* Other `RequestException`s are mapped to the appropriate custom error based on the HTTP status code (401/403 → `ForbiddenError`, 429 → `ConflictError`, others → `SomethingWrongError`).  
* Any other exception becomes a generic `SomethingWrongError`.  

In short, the method safely downloads a file, enforces security and size limits, validates the content, and returns a fully‑described `RawFile` object.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
