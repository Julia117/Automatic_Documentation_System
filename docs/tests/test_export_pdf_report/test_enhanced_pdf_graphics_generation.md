# test_enhanced_pdf_graphics_generation (function)

**Code:**
```python
def test_enhanced_pdf_graphics_generation(sample_data):
    """Test that graphics are actually generated when libraries are available."""
    match_response, instruments, tmp_path = sample_data
    out_file = tmp_path / "enhanced_with_real_graphics.pdf"

    with patch('harmony.services.export_pdf_report.create_match_distribution_chart') as mock_chart:
        mock_fig = MagicMock()
        mock_chart.return_value = mock_fig
        
        generate_harmony_pdf_report(
            match_response, instruments, filename=str(out_file),
            threshold=0.5, include_graphics=True
        )
        
        # Verify chart creation was attempted
        mock_chart.assert_called_once()
```

**Explanation:**
**Function Explanation: `test_enhanced_pdf_graphics_generation`**

This function is a test case that checks if graphics are generated when the necessary libraries are available.

**What it does:**

1. It takes some sample data (`sample_data`) as input.
2. It creates a temporary file path (`out_file`) where the generated PDF will be saved.
3. It uses a mocking library (`patch`) to simulate the creation of a chart (`create_match_distribution_chart`) in the `harmony.services.export_pdf_report` module.
4. It calls the `generate_harmony_pdf_report` function with the sample data, specifying that graphics should be included (`include_graphics=True`).
5. It verifies that the chart creation was attempted by checking if the `mock_chart` was called once.

**In simple terms:**

This test case checks if the `generate_harmony_pdf_report` function can generate graphics when the necessary libraries are available. It does this by simulating the creation of a chart and verifying that it was attempted.

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
