# UnauthorizedError (class)

**Code:**
```python
class UnauthorizedError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 401
        self.detail = message or "Unauthorized"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**UnauthorizedError Class Explanation**

This class represents an error that occurs when a user is not authorized to access a resource. It's a custom exception class that inherits from `BaseHarmonyError`.

**Key Features:**

1. **Status Code**: The error has a status code of 401, which is the standard HTTP status code for unauthorized access.
2. **Error Message**: The error message is customizable, but defaults to "Unauthorized" if no message is provided.
3. **Inheritance**: The class inherits from `BaseHarmonyError`, which provides a basic structure for error handling.

**Usage:**

To use this class, you can raise an instance of `UnauthorizedError` when a user is not authorized to access a resource. For example:
```python
raise UnauthorizedError("Invalid username or password")
```
This will raise an error with a status code of 401 and a custom error message.

