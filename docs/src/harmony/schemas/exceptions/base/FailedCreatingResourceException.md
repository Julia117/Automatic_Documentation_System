# FailedCreatingResourceException (class)

**Code:**
```python
class FailedCreatingResourceException(Exception):
    def __init__(self, message: str = None):
        self.status_code = 400
        if not message:
            message = "Failed when creating resource."
        self.message = message
        super().__init__(message)
```

**Explanation:**
**`FailedCreatingResourceException` – quick rundown**

- **What it is**: A custom exception that signals a failure when trying to create a new resource (e.g., a database record, file, or API object).
- **Key features**:
  - Inherits from Python’s built‑in `Exception`.
  - Sets an HTTP‑style `status_code` of **400** (Bad Request) so callers can map it to an HTTP response.
  - Accepts an optional `message`. If none is supplied, it defaults to `"Failed when creating resource."`.
  - Stores that message in `self.message` and passes it to the base `Exception` constructor so the exception’s string representation is the message.

**Why use it?**  
When your code attempts to create a resource and something goes wrong (validation error, missing data, etc.), raising this exception makes the error explicit, provides a clear default message, and gives a standard status code that can be translated into an HTTP response or logged consistently.

