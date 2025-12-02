# chapter_title (function)

**Code:**
```python
def chapter_title(self, title: str, color: Tuple[int, int, int] = (31, 81, 155)):
        """Add a chapter title with colored background."""
        self.set_font("Arial", "B", 14)
        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, sanitize(title), ln=True, fill=True, align="L")
        self.set_text_color(0, 0, 0)
        self.ln(5)
```

**Explanation:**
**Function Explanation: `chapter_title`**

This function adds a chapter title to a PDF document with a colored background. Here's a step-by-step breakdown:

1. **Set font and style**: The function sets the font to "Arial" with a bold style and size 14.
2. **Set fill color**: The function sets the fill color of the background to the specified color (default is blue).
3. **Set text color**: The function sets the text color to white.
4. **Add title**: The function adds the chapter title to the PDF document with the specified color and alignment (left).
5. **Reset text color**: The function resets the text color to black.
6. **Add line break**: The function adds a line break (5 units) to move to the next line.

In summary, this function creates a visually appealing chapter title with a colored background and white text.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
