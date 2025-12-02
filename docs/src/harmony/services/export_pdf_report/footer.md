# footer (function)

**Code:**
```python
def footer(self):
        """Add page footer with page numbers."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        self.set_text_color(0, 0, 0)
```

**Explanation:**
This function, `footer(self)`, is used to add a footer to a PDF document. It includes the following features:

- It sets the font to Arial, in italic style, with a size of 8 points.
- It sets the text color to a light gray (128, 128, 128).
- It adds the current page number to the footer, centered horizontally.
- Finally, it resets the text color to black (0, 0, 0).

In simpler terms, this function adds a footer to a PDF document that displays the current page number.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
