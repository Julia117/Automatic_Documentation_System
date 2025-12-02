# empty_match_data (function)

**Code:**
```python
def empty_match_data(tmp_path):
    """Create test data with no matches above threshold."""
    instruments = [
        create_instrument_from_list(
            ["Completely unrelated question about weather"],
            [],
            instrument_name="Weather Survey"
        ),
        create_instrument_from_list(
            ["Question about cooking preferences"],
            [],
            instrument_name="Cooking Survey"
        )
    ]
    match_response = match_instruments(instruments)
    return match_response, instruments, tmp_path
```

**Explanation:**
**Function Explanation: `empty_match_data(tmp_path)`**

This function generates test data for matching instruments with no matches above a certain threshold. It creates two test instruments, "Weather Survey" and "Cooking Survey", each with a single question and no answers. The function then calls the `match_instruments` function to match these instruments and returns the match response, the created instruments, and the temporary path (`tmp_path`) used for testing.

In simple terms, this function sets up a test scenario where two instruments are created with no matching answers, and then it runs the matching algorithm to see how it handles this scenario. The returned values can be used to test the functionality of the matching algorithm.

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
