# ConflictError (class)

**Code:**
```python
class ConflictError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 409
        self.detail = message or "Conflict"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**ConflictError – a quick‑look**

- **What it is**  
  A custom exception that signals an HTTP **409 Conflict** situation (e.g., trying to create a resource that already exists).

- **How it works**  
  ```python
  class ConflictError(BaseHarmonyError):
      def __init__(self, message: str = None):
          self.status_code = 409          # HTTP status code
          self.detail = message or "Conflict"   # human‑readable message
          super(Exception, self).__init__(self.detail)
  ```
  * It inherits from `BaseHarmonyError`, so it already behaves like a normal Python exception.
  * The constructor sets `status_code` to **409** and stores a message (`detail`).  
  * If no message is supplied, it defaults to `"Conflict"`.
  * The `super(Exception, self).__init__(self.detail)` call simply forwards the message to the base `Exception` constructor (the `BaseHarmonyError` constructor is not called here, but the message is still stored in the exception object).

- **When to use it**  
  Raise `ConflictError` whenever an operation cannot proceed because the requested state already exists or conflicts with the current state. The framework can catch this exception and automatically return a 409 response to the client.

