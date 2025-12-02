# ResourceNotFoundError (class)

**Code:**
```python
class ResourceNotFoundError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 404
        self.detail = message or "Resource not found"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**ResourceNotFoundError** is a custom exception you can raise when a requested resource can’t be found.

- **Inherits** from `BaseHarmonyError`, so it behaves like a normal Python exception but also carries HTTP‑style metadata.
- **`status_code = 404`** – tells callers (e.g., an API layer) that this is a “Not Found” error.
- **`detail`** – the human‑readable message. If you pass a string it uses that; otherwise it defaults to `"Resource not found"`.
- **`super(Exception, self).__init__(self.detail)`** – passes the message to the base `Exception` constructor so the exception’s string representation is the detail text.

Use it like:

```python
raise ResourceNotFoundError("User with id 42 does not exist")
```

or simply:

```python
raise ResourceNotFoundError()
```

and the caller can inspect `e.status_code` and `e.detail` to generate an appropriate HTTP response.

