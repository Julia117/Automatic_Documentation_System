# UnauthorizedException (class)

**Code:**
```python
class UnauthorizedException(Exception):
    def __init__(self, message: str = None):
        self.status_code = 401
        if not message:
            message = "Unauthorized"
        self.message = message
        super().__init__(message)
```

**Explanation:**
**`UnauthorizedException` – a simple custom error**

- **What it is**: A Python exception that signals an HTTP 401 “Unauthorized” error.
- **Key features**:
  - Inherits from the built‑in `Exception` class.
  - Sets an attribute `status_code = 401` so callers can read the HTTP status.
  - Accepts an optional `message`. If you don’t pass one, it defaults to `"Unauthorized"`.
  - Stores the message in `self.message` and passes it to the base `Exception` constructor so the error text is available via `str(e)` or `e.args`.

**When to use it**  
Raise `UnauthorizedException()` (or with a custom message) whenever a request fails authentication, e.g.:

```python
if not user.is_authenticated:
    raise UnauthorizedException()
```

The caller can catch it, read `e.status_code` (401), and return the appropriate HTTP response.

