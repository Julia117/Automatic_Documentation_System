# ResourceNotFoundException (class)

**Code:**
```python
class ResourceNotFoundException(Exception):
    def __init__(self, message: str = None):
        self.status_code = 404
        if not message:
            message = "Resource not found"
        self.message = message
        super().__init__(message)
```

**Explanation:**
**ResourceNotFoundException**  
A tiny custom error you can raise when a requested resource can’t be found.

- **Inherits** from Python’s built‑in `Exception`.  
- **`status_code = 404`** – handy if you’re building an API; the exception carries the HTTP status code.  
- **Default message** – if you don’t pass a message, it uses `"Resource not found"`.  
- **`self.message`** stores the final message for easy access.  
- Calls `super().__init__(message)` so the exception behaves like a normal one.

Use it like:

```python
if not resource:
    raise ResourceNotFoundException()          # or with a custom message
```

It’s a clean way to signal “not found” errors while keeping the HTTP status code attached.

