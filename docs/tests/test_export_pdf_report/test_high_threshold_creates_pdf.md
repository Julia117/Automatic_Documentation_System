# test_high_threshold_creates_pdf (function)

**Code:**
```python
def test_high_threshold_creates_pdf(sample_data):
    """Test original function with high threshold (existing test)."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "report_high_thresh.pdf"

    result_path = generate_pdf_report(
        match_response, instruments, filename=str(out_file), threshold=0.99
    )

    assert out_file.exists(), "PDF file was not created"
    assert out_file.stat().st_size > 0, "PDF file is empty"
    assert result_path == str(out_file.resolve()), "Returned path should match input"
```

**Explanation:**
This function is a test case for a PDF report generation function. It checks if a PDF file is created when the threshold is set to a high value (0.99). 

Here's a step-by-step breakdown:

1. It takes some sample data (`sample_data`) which includes a match response, instruments, and a temporary path.
2. It creates a new PDF file named "report_high_thresh.pdf" in the temporary path.
3. It calls the `generate_pdf_report` function with the match response, instruments, the PDF file path, and a high threshold (0.99).
4. It checks if the PDF file exists and is not empty.
5. It checks if the returned path from the `generate_pdf_report` function matches the expected path of the PDF file.

In simple terms, this function is testing if the PDF report generation function works correctly when the threshold is set to a high value.

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
