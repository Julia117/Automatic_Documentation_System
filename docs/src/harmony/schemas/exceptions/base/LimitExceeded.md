# LimitExceeded (class)

**Code:**
```python
class LimitExceeded(Exception):
    def __init__(self, message: str = None):
        self.status_code = 401
        if not message:
            message = "Too many requests, try again later."
        self.message = message
        super().__init__(message)
```

**Explanation:**
**LimitExceeded** is a tiny custom exception you can raise when a user has hit a rate‑limit or request quota.  
- It inherits from Python’s built‑in `Exception`.  
- When you create it, it automatically sets a `status_code` of **401** (you could change this to 429 if you prefer).  
- If you don’t supply a message, it defaults to “Too many requests, try again later.”  
- The message is stored in `self.message` and passed to the base `Exception` constructor so it shows up in stack traces and logs.  

Use it like:

```python
if request_count > MAX_REQUESTS:
    raise LimitExceeded()
```

This lets your error‑handling middleware or API layer return a clear, consistent error to the client.

