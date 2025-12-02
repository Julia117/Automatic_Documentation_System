# BaseException (class)

**Code:**
```python
class BaseException(Exception):
    status_code = 500
    message = "Something went wrong"
```

**Explanation:**
**BaseException**

- **What it is**: A custom exception class that inherits from Python’s built‑in `Exception`.
- **Purpose**: Provides a common starting point for all other error types in the project.
- **Key attributes**:
  - `status_code = 500` – the default HTTP status code (Internal Server Error).
  - `message = "Something went wrong"` – a default human‑readable error message.
- **How it’s used**: Other error classes can inherit from `BaseException` (or `BaseHarmonyError`) to automatically get these defaults, then override `status_code` or `message` as needed. This keeps error handling consistent across the codebase.

