# test_graphics_fallback_when_unavailable (function)

**Code:**
```python
def test_graphics_fallback_when_unavailable(sample_data):
    """Test that the function gracefully handles missing graphics libraries."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "no_graphics_fallback.pdf"

    # Mock GRAPHICS_AVAILABLE to False
    with patch('harmony.services.export_pdf_report.GRAPHICS_AVAILABLE', False):
        result_path = generate_harmony_pdf_report(
            match_response, instruments, filename=str(out_file),
            threshold=0.5, include_graphics=True  # Request graphics but they're unavailable
        )

    assert out_file.exists(), "PDF should be created even without graphics"
    assert out_file.stat().st_size > 0, "PDF should have content even without graphics"
```

**Explanation:**
**Function Explanation: `test_graphics_fallback_when_unavailable`**

This function tests the behavior of the `generate_harmony_pdf_report` function when graphics libraries are not available. It simulates a scenario where graphics are requested but cannot be used.

Here's a step-by-step breakdown:

1. It takes some sample data (`sample_data`) as input, which includes a match response, instruments, and a temporary path.
2. It creates a file path (`out_file`) where the PDF report will be saved.
3. It uses a `patch` to mock the `GRAPHICS_AVAILABLE` variable to `False`, indicating that graphics libraries are not available.
4. It calls the `generate_harmony_pdf_report` function with the match response, instruments, and the file path, requesting graphics (`include_graphics=True`) despite the libraries being unavailable.
5. It asserts that the PDF file exists and has content, even though graphics are not available.

In simple terms, this function ensures that the `generate_harmony_pdf_report` function can still produce a valid PDF report even when graphics libraries are not available.

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
