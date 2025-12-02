# ForbiddenException (class)

**Code:**
```python
class ForbiddenException(Exception):
    def __init__(self, message: str = None):
        self.status_code = 403
        if not message:
            message = "Forbidden"
        self.message = message
        super().__init__(message)
```

**Explanation:**
**ForbiddenException** is a tiny helper that turns a “403 Forbidden” error into a Python exception.

- **Inherits from** `Exception`, so it behaves like any normal error you can `raise` or `except`.
- **`status_code = 403`** – stores the HTTP status code that the exception represents.
- **Default message** – if you don’t pass a message, it uses the string `"Forbidden"`.
- **`self.message`** – keeps the human‑readable text for later inspection or logging.
- **`super().__init__(message)`** – passes the message to the base `Exception` so that the standard exception machinery (e.g., `str(e)`) works.

**Typical use**

```python
def get_resource(user):
    if not user.has_access:
        raise ForbiddenException()          # or ForbiddenException("You can't view this")
```

When caught, you can read `e.status_code` (403) and `e.message` (“Forbidden”) to build an HTTP response.

