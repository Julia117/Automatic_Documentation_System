# header (function)

**Code:**
```python
def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(31, 81, 155) 
        self.cell(0, 12, sanitize("Harmony Harmonisation Report"), ln=True, align="C")
        self.set_text_color(0, 0, 0) 
        self.set_font("Arial", "", 10)
        self.cell(
            0, 8,
            sanitize(f"Generated on {datetime.now():%Y-%m-%d %H:%M:%S}"),
            ln=True, align="C"
        )
        self.ln(8)
```

**Explanation:**
**Function Explanation: `header(self)`**

This function is used to create a header for a PDF report. It sets the font, text color, and adds the report title and generation date to the PDF.

Here's a step-by-step breakdown:

1. **Set font**: Sets the font to "Arial" with bold style and size 16.
2. **Set text color**: Sets the text color to a specific blue color (31, 81, 155).
3. **Add report title**: Adds the report title "Harmony Harmonisation Report" to the PDF, centered and on a new line.
4. **Reset text color**: Resets the text color to black (0, 0, 0).
5. **Set font (again)**: Sets the font to "Arial" with regular style and size 10.
6. **Add generation date**: Adds the current date and time to the PDF, centered and on a new line.
7. **Add line spacing**: Adds 8 units of line spacing to move to the next section of the report.

This function is likely used in a PDF generation class to create a consistent header for all reports.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
