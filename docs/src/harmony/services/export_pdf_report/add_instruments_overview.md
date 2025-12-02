# add_instruments_overview (function)

**Code:**
```python
def add_instruments_overview(self, instruments: List[Instrument], match_stats: dict):
        """Enhanced instruments overview with statistics."""
        self.chapter_title("Instruments Overview")
        
        # Table header
        self.set_font("Arial", "B", 10)
        self.set_fill_color(230, 230, 230)
        
        col_widths = [60, 30, 40, 60]
        headers = ["Instrument Name", "Questions", "Matches Found", "Avg Match Score"]
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, sanitize(header), border=1, fill=True)
        self.ln()
        
        # Table rows
        self.set_font("Arial", "", 9)
        self.set_fill_color(255, 255, 255)
        
        for inst in instruments:
            name = inst.instrument_name or "Unnamed Instrument"
            q_count = len(inst.questions) if inst.questions else 0
            
            # Get stats for this instrument
            inst_matches = match_stats.get('by_instrument', {}).get(name, {})
            matches_found = inst_matches.get('matches', 0)
            avg_score = inst_matches.get('avg_score', 0)
            
            # Truncate long names
            display_name = name[:22] + "..." if len(name) > 25 else name
            
            self.cell(col_widths[0], 8, sanitize(display_name), border=1)
            self.cell(col_widths[1], 8, sanitize(str(q_count)), border=1, align="C")
            self.cell(col_widths[2], 8, sanitize(str(matches_found)), border=1, align="C")
            self.cell(col_widths[3], 8, sanitize(f"{avg_score:.1f}%"), border=1, align="C")
            self.ln()
        
        self.ln(5)
```

**Explanation:**
This function, `add_instruments_overview`, generates a table in a PDF report that provides an overview of the instruments used in the analysis. The table includes the following columns:

1. Instrument Name: The name of the instrument.
2. Questions: The number of questions in the instrument.
3. Matches Found: The number of matches found for the instrument.
4. Avg Match Score: The average match score for the instrument.

The function takes two parameters:

1. `instruments`: A list of instruments used in the analysis.
2. `match_stats`: A dictionary containing statistics about the matches found for each instrument.

The function uses the `sanitize` function to ensure that the instrument names are displayed correctly in the table, and it truncates long instrument names to fit within the table cell.

The function is likely used in a PDF report generation context, where it is used to display the instrument overview in a clear and concise manner.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
