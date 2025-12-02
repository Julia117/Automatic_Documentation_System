# BadRequestError (class)

**Code:**
```python
class BadRequestError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 400
        self.detail = message or "Bad request data"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**BadRequestError Class Explanation**

This class represents a custom error in a web application, specifically for bad request data. It's a subclass of `BaseHarmonyError`.

**Key Features:**

1. **Status Code**: Sets the HTTP status code to 400, indicating a bad request.
2. **Error Message**: Provides a default error message "Bad request data" or allows a custom message to be passed in the constructor.
3. **Inheritance**: Inherits from `BaseHarmonyError`, which provides a basic error handling structure.

**Usage:**

To use this class, you can create an instance of `BadRequestError` and pass a custom error message, like this:
```python
try:
    # Code that might raise an error
except BadRequestError as e:
    print(e.detail)  # Output: "Bad request data"
```
Or, you can pass a custom error message:
```python
try:
    # Code that might raise an error
except BadRequestError as e:
    print(e.detail)  # Output: "Invalid username or password"
```

