# ForbiddenError (class)

**Code:**
```python
class ForbiddenError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 403
        self.detail = message or "Forbidden"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**ForbiddenError – a custom “403 Forbidden” exception**

- **What it is**: A Python exception that represents an HTTP 403 (Forbidden) error.
- **Inheritance**: It subclasses `BaseHarmonyError`, which in turn subclasses the built‑in `Exception`.  
- **What it does**:
  1. Sets `self.status_code` to `403` so callers can inspect the HTTP status.
  2. Stores a human‑readable message in `self.detail`. If no message is supplied, it defaults to `"Forbidden"`.
  3. Calls the base `Exception` constructor with that message, so the exception can be raised and caught like any normal Python error.

Use it when your code needs to signal that a request is not allowed (e.g., missing permissions). It carries both the status code and a clear error message for logging or API responses.

