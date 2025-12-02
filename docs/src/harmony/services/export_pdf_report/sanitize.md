# sanitize (function)

**Code:**
```python
def sanitize(text: str) -> str:
    """Sanitizer text for pdf output, handling None values and encoding issues."""
    if text is None:
        return ""
    return str(text).encode("latin-1", "ignore").decode("latin-1")
```

**Explanation:**
**Function Explanation: `sanitize`**

This function takes a string input `text` and returns a sanitized version of it. Here's what it does:

1. If the input `text` is `None`, it returns an empty string (`""`).
2. If the input `text` is not `None`, it converts it to a string using `str(text)`.
3. It then encodes the string using the `latin-1` encoding scheme with the `ignore` error handler. This means that any characters that can't be encoded in `latin-1` will be ignored.
4. Finally, it decodes the encoded string back to a regular string using the `latin-1` encoding scheme.

**Purpose:**

The purpose of this function is to handle encoding issues and `None` values when generating PDF output. It ensures that the input text is a valid string that can be safely used in a PDF document.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
