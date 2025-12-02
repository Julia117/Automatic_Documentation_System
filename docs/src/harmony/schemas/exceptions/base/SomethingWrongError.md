# SomethingWrongError (class)

**Code:**
```python
class SomethingWrongError(BaseHarmonyError):
    def __init__(self, message: str = None):
        self.status_code = 500
        self.detail = message or "Something went wrong"
        super(Exception, self).__init__(self.detail)
```

**Explanation:**
**SomethingWrongError Class Explanation**

This class represents a custom error in a Python application. It's designed to handle situations where something unexpected goes wrong.

**Key Features:**

1. **Error Code**: It sets the HTTP status code to 500, indicating a server-side error.
2. **Error Message**: It provides a default error message "Something went wrong" or allows a custom message to be passed in the constructor.
3. **Inheritance**: It inherits from `BaseHarmonyError`, which is a custom exception class.

**Usage:**

To use this class, you can create an instance of `SomethingWrongError` and pass a custom error message, like this:
```python
try:
    # code that might raise an error
except SomethingWrongError as e:
    print(e.detail)  # prints the custom error message
```
This class is useful for catching and handling unexpected errors in your application, providing a clear and consistent error message to the user.

