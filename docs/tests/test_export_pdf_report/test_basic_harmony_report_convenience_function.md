# test_basic_harmony_report_convenience_function (function)

**Code:**
```python
def test_basic_harmony_report_convenience_function(sample_data):
    """Test the convenience function for basic reports."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "basic_harmony_report.pdf"

    result_path = generate_basic_harmony_report(
        match_response, instruments, filename=str(out_file)
    )

    assert out_file.exists(), "Basic harmony report was not created"
    assert out_file.stat().st_size > 0, "Basic harmony report is empty"
```

**Explanation:**
**Function Explanation: `test_basic_harmony_report_convenience_function`**

This function is a test case that verifies the functionality of a convenience function called `generate_basic_harmony_report`. The purpose of this function is to generate a basic harmony report in PDF format.

Here's a step-by-step breakdown:

1. It takes in some sample data (`sample_data`) which contains three variables: `match_response`, `instruments`, and `tmp_path`.
2. It creates a temporary file path (`out_file`) where the report will be saved.
3. It calls the `generate_basic_harmony_report` function, passing in the `match_response`, `instruments`, and the temporary file path.
4. It asserts that the temporary file exists and is not empty, indicating that the report was successfully generated.

In simple terms, this function is testing whether the `generate_basic_harmony_report` function can correctly generate a basic harmony report in PDF format.

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
