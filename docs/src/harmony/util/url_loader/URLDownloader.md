# URLDownloader (class)

**Code:**
```python
class URLDownloader:
    def __init__(self):
        self.rate_limit_storage: Dict[str, List[datetime]] = {}
        self.session = requests.Session()
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        self.session.verify = True

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

    def _validate_ssl(self, response: requests.Response) -> None:
        cert = response.raw.connection.sock.getpeercert()
        if not cert:
            raise ForbiddenError("Invalid SSL certificate")

        not_after = ssl.cert_time_to_seconds(cert['notAfter'])
        if datetime.fromtimestamp(not_after) < datetime.now():
            raise ForbiddenError("Expired SSL certificate")

    def _check_legal_headers(self, response: requests.Response) -> None:
        if response.headers.get('X-Robots-Tag', '').lower() == 'noindex':
            raise ForbiddenError("Access not allowed by robots directive")

        if 'X-Copyright' in response.headers:
            raise ForbiddenError("Content is copyright protected")

        if 'X-Terms-Of-Service' in response.headers:
            raise ForbiddenError("Terms of service acceptance required")

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
**URLDownloader – quick‑start guide**

| What it does | How it works | Why it matters |
|--------------|--------------|----------------|
| **Downloads a file from a URL** | 1. **Validate the URL** – checks scheme, domain, path safety, fragments, and blocks internal hosts. <br>2. **Rate‑limit per domain** – keeps a timestamp list for each host; if too many requests in the window it raises `ConflictError`. <br>3. **HTTP GET** – uses a `requests.Session` with 3 retries, custom User‑Agent, and accepts only whitelisted MIME types. <br>4. **SSL & legal checks** – verifies the server certificate is present and not expired; rejects responses that set `X‑Robots‑Tag: noindex`, `X‑Copyright`, or `X‑Terms‑Of‑Service`. <br>5. **File size & type** – rejects files larger than `MAX_FILE_SIZE`; determines the file type from the `Content‑Type` header or file extension. <br>6. **Read & hash** – streams the body, updates a SHA‑256 hash, and stores the content. Binary files (PDF, XLSX, DOCX) are base64‑encoded; text files are decoded as UTF‑8. <br>7. **Return** – a `RawFile` object containing a UUID, original file name, file type, content, and metadata (hash, timestamp, source URL). | Ensures only safe, legal, and reasonably sized files are fetched, protects against abuse (rate limits), and provides a consistent, hash‑verified payload for downstream processing. |

**Key methods**

* `__init__` – sets up the session and an empty rate‑limit store.  
* `_check_rate_limit(domain)` – cleans old timestamps, enforces `RATE_LIMIT_REQUESTS` per `RATE_LIMIT_WINDOW`.  
* `_validate_url(url)` – parses the URL and raises `BadRequestError` or `ForbiddenError` on violations.  
* `_validate_ssl(response)` – checks the peer certificate and expiration.  
* `_check_legal_headers(response)` – blocks content flagged by robots, copyright, or terms headers.  
* `_validate_content_type(url, content_type)` – maps MIME or file extension to a `FileType`; otherwise raises `BadRequestError`.  
* `download(url)` – orchestrates the whole flow, handles `requests` exceptions, and returns a `RawFile`.

**Error handling**

* `BadRequestError`, `ForbiddenError`, `ConflictError` are re‑raised unchanged.  
* Network issues (`Timeout`, `TooManyRedirects`, `RequestException`) are translated into `SomethingWrongError` or `ForbiddenError` with clear messages.  
* HTTP status codes 401/403 → `ForbiddenError`; 429 → `ConflictError`; others → `SomethingWrongError`.

**Why use it?**

- **Security** – blocks unsafe URLs, internal hosts, path traversal, and expired certificates.  
- **Compliance** – respects robots.txt, copyright, and terms headers.  
- **Robustness** – streams large files, limits size, and retries transient failures.  
- **Consistency** – always returns a `RawFile` with a verified hash and metadata for downstream consumers.

**Imports:**
```
import base64, import hashlib, import requests, import ssl, import urllib.parse, import uuid, from datetime import datetime, timedelta, from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments, from harmony.schemas.errors.base import BadRequestError, ForbiddenError, ConflictError, SomethingWrongError, from harmony.schemas.requests.text import RawFile, Instrument, FileType, from pathlib import Path, from requests.adapters import HTTPAdapter, from typing import List, Dict
```
