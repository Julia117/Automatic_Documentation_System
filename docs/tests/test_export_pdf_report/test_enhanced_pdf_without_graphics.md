# test_enhanced_pdf_without_graphics (function)

**Code:**
```python
def test_enhanced_pdf_without_graphics(sample_data):
    """Test new enhanced function with graphics disabled."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "enhanced_report_no_graphics.pdf"

    result_path = generate_harmony_pdf_report(
        match_response, instruments, filename=str(out_file),
        threshold=0.5, include_graphics=False
    )

    assert out_file.exists(), "Enhanced PDF file was not created"
    assert out_file.stat().st_size > 0, "Enhanced PDF file is empty"
```

**Explanation:**
**Function Explanation: `test_enhanced_pdf_without_graphics`**

This function tests the `generate_harmony_pdf_report` function with graphics disabled. Here's a step-by-step breakdown:

1. It takes in `sample_data`, which contains three variables: `match_response`, `instruments`, and `tmp_path`.
2. It creates a temporary file path `out_file` with the name "enhanced_report_no_graphics.pdf" in the `tmp_path` directory.
3. It calls the `generate_harmony_pdf_report` function with the following parameters:
	* `match_response`
	* `instruments`
	* `filename` set to the `out_file` path
	* `threshold` set to 0.5
	* `include_graphics` set to `False` (disabled)
4. It asserts that the `out_file` exists and has a non-zero size, indicating that the PDF file was created successfully.

In simple terms, this function tests that the `generate_harmony_pdf_report` function can create a PDF file without graphics when requested.

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
