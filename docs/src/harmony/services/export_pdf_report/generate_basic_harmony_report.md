# generate_basic_harmony_report (function)

**Code:**
```python
def generate_basic_harmony_report(
    match_response: MatchResponse,
    instruments: List[Instrument],
    filename: str = "harmony_report.pdf",
    threshold: float = 0.5
) -> str:
    """Generate a basic harmonisation report without graphics (faster generation)."""
    return generate_harmony_pdf_report(
        match_response=match_response,
        instruments=instruments,
        filename=filename,
        threshold=threshold,
        include_graphics=False,
        max_matches_displayed=30
    )
```

**Explanation:**
This function generates a basic harmonization report without graphics. It's a convenience function that calls another function (`generate_harmony_pdf_report`) with specific parameters to produce a faster report. The report includes a summary of harmonized question pairs, but without charts or graphics.

**Imports:**
```
import os, import io, from datetime import datetime, from typing import List, Optional, Tuple, import tempfile, from fpdf import FPDF, from harmony.schemas.requests.text import Instrument, from harmony.schemas.responses.text import MatchResponse
```
