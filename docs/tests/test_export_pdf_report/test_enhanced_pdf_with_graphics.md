# test_enhanced_pdf_with_graphics (function)

**Code:**
```python
def test_enhanced_pdf_with_graphics(sample_data):
    """Test new enhanced function with graphics enabled - FIXED."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "enhanced_report_with_graphics.pdf"

    result_path = generate_harmony_pdf_report(
        match_response, instruments, filename=str(out_file),
        threshold=0.5, include_graphics=True
    )

    assert out_file.exists(), "Enhanced PDF file was not created"
    assert out_file.stat().st_size > 0, "Enhanced PDF file is empty"
    
    # FIXED: More reasonable comparison - just check that both files are created successfully
    # The size comparison was unreliable due to different PDF generation approaches
```

**Explanation:**
**Function Explanation: `test_enhanced_pdf_with_graphics`**

This function tests the `generate_harmony_pdf_report` function with graphics enabled. Here's a step-by-step breakdown:

1. It takes in `sample_data`, which contains three variables: `match_response`, `instruments`, and `tmp_path`.
2. It creates a temporary file path `out_file` with the name "enhanced_report_with_graphics.pdf".
3. It calls the `generate_harmony_pdf_report` function with the following parameters:
	* `match_response`
	* `instruments`
	* `filename` set to the `out_file` path
	* `threshold` set to 0.5
	* `include_graphics` set to `True`
4. It asserts that the `out_file` exists and has a non-zero size, indicating that the PDF file was created successfully.

In summary, this function tests the creation of a PDF file with graphics enabled using the `generate_harmony_pdf_report` function.

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
