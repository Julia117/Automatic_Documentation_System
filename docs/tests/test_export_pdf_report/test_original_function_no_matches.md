# test_original_function_no_matches (function)

**Code:**
```python
def test_original_function_no_matches(empty_match_data):
    """Test original function when no matches are found."""
    match_response, instruments, tmp_path = empty_match_data
    out_file = tmp_path / "no_matches.pdf"

    result_path = generate_pdf_report(
        match_response, instruments, filename=str(out_file), threshold=0.5
    )

    assert out_file.exists(), "PDF should be created even with no matches"
    assert out_file.stat().st_size > 0, "PDF should have content even with no matches"
```

**Explanation:**
This function tests the original PDF report generation function (`generate_pdf_report`) when no matches are found. 

Here's a simplified explanation:

1. It takes some pre-defined data (`empty_match_data`) that simulates a scenario with no matches.
2. It generates a PDF report using the `generate_pdf_report` function, specifying a threshold of 0.5.
3. It checks two things:
   - If the PDF file is created successfully.
   - If the PDF file has any content (i.e., it's not empty).

In essence, this function ensures that the original PDF report generation function behaves correctly even when no matches are found.

**Imports:**
```
import pytest, import os, import warnings, from pathlib import Path, from unittest.mock import patch, MagicMock, from harmony.services.export_pdf_report import (
    generate_pdf_report, 
    generate_harmony_pdf_report, 
    generate_basic_harmony_report, 
    calculate_harmonisation_statistics,
    GRAPHICS_AVAILABLE
), from harmony import create_instrument_from_list, example_instruments, match_instruments
```
