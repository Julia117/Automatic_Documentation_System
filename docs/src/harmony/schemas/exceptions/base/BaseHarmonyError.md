# BaseHarmonyError (class)

**Code:**
```python
class BaseHarmonyError(Exception):
    def __init__(self, message: str = None):
        self.status_code = 500
        self.detail = message or "Something went wrong"
        super().__init__(self.detail)
```

**Explanation:**
**BaseHarmonyError Class Explanation**

The `BaseHarmonyError` class is a custom exception class that inherits from Python's built-in `Exception` class. It's designed to handle errors in a specific way, providing a standardized structure for error messages and status codes.

**Key Features:**

1. **Status Code**: Each instance of `BaseHarmonyError` has a `status_code` attribute, which defaults to 500 (Internal Server Error). This can be overridden to represent a specific HTTP status code.
2. **Error Message**: The `detail` attribute stores a human-readable error message, which defaults to "Something went wrong" if no message is provided. This message can be customized to provide more context about the error.
3. **Inheritance**: By inheriting from `Exception`, `BaseHarmonyError` can be raised as an exception in your code, allowing you to catch and handle errors in a centralized way.

**Usage:**

To use `BaseHarmonyError`, simply create an instance and pass a custom error message (if desired):
```python
try:
    # Code that might raise an error
except BaseHarmonyError as e:
    print(f"Error: {e.detail} (Status Code: {e.status_code})")
```
By using `BaseHarmonyError` as a base class, you can create more specific error classes (like `ConflictError` or `BadRequestError`) that inherit its behavior and add their own customizations.

