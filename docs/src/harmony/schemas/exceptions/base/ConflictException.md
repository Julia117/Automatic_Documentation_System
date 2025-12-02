# ConflictException (class)

**Code:**
```python
class ConflictException(Exception):
    def __init__(self, message: str = None):
        self.status_code = 409
        if not message:
            message = "Conflict"
        self.message = message
        super().__init__(message)
```

**Explanation:**
**ConflictException** is a tiny custom error you can raise when two operations clash (e.g., two users try to create the same resource).  
- It inherits from Python’s built‑in `Exception`.  
- When you instantiate it, it automatically sets `status_code = 409` (the HTTP “Conflict” code).  
- If you don’t pass a message, it defaults to `"Conflict"`.  
- The message is stored in `self.message` and passed to the base `Exception` constructor so it shows up in stack traces.  

Use it whenever you need to signal a 409 Conflict in your API or business logic.

