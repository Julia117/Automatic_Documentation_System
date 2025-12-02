# sample_data (function)

**Code:**
```python
def sample_data(tmp_path):
    """Create sample test data for PDF generation tests."""
    gad_7_norwegian = create_instrument_from_list(
        [
            "Følt deg nervøs, engstelig eller veldig stresset",
            "Ikke klart å slutte å bekymre deg eller kontrolleren bekymringene dine"
        ],
        [],
        instrument_name="GAD-7 Norwegian"
    )
    instruments = [
        example_instruments["CES_D English"],
        example_instruments["GAD-7 Portuguese"],
        gad_7_norwegian
    ]
    match_response = match_instruments(
        instruments,
        topics=["anxiety", "nervous", "difficulty", "scared", "unhappy", "sleep", "eating"]
    )
    return match_response, instruments, tmp_path
```

**Explanation:**
This function, `sample_data(tmp_path)`, generates sample test data for PDF generation tests. It creates three instruments with Norwegian, English, and Portuguese translations of the GAD-7 questionnaire, and then matches these instruments against a set of predefined topics. The function returns the match response, the list of instruments, and the temporary path used for testing.

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
