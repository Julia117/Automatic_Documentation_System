# __init__ (function)

**Code:**
```python
def __init__(self, message: str = None):
        self.status_code = 500
        self.detail = message or "Something went wrong"
        super().__init__(self.detail)
```

**Explanation:**
**Function Explanation:**

This is a special function in Python called a constructor (`__init__`) that is used to initialize an object of a class.

**What it does:**

1. It sets the `status_code` attribute to 500, which is a standard HTTP error code for "Internal Server Error".
2. It sets the `detail` attribute to a message. If no message is provided, it defaults to "Something went wrong".
3. It calls the parent class's (`super()`) constructor with the `detail` message, passing it down the inheritance chain.

**In simple terms:**

This function creates a new error object with a default status code of 500 and a default error message of "Something went wrong". If a custom message is provided, it will use that instead.

