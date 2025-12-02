# test_crosswalk_two_instruments_enforce_one_to_one_matches (function)

**Code:**
```python
def test_crosswalk_two_instruments_enforce_one_to_one_matches(self):

        instrument_1 = create_instrument_from_list(["I felt fearful."], [])
        instrument_2 = create_instrument_from_list(
            ["Feeling afraid, as if something awful might happen", "Feeling nervous, anxious, or on edge"],
            [])
        instruments = [instrument_1, instrument_2]

        match_response = match_instruments(instruments)
        result = generate_crosswalk_table(instruments, match_response.similarity_with_polarity, 0,
                                          is_enforce_one_to_one=True)

        self.assertEqual(1, len(result))
```

**Explanation:**
This function tests the `generate_crosswalk_table` function when two instruments are matched and the `is_enforce_one_to_one` parameter is set to `True`. 

In simple terms, it checks if the function correctly generates a crosswalk table where each question from one instrument is matched to only one question from the other instrument, resulting in a table with a single row. 

The test creates two instruments, matches them, and then generates a crosswalk table with the `is_enforce_one_to_one` parameter set to `True`. It then asserts that the resulting table has only one row, indicating that each question from one instrument is matched to only one question from the other instrument.

**Imports:**
```
import sys, import unittest, import numpy as np, import pandas as pd, from harmony.matching.generate_crosswalk_table import generate_crosswalk_table, from harmony import create_instrument_from_list, from harmony import match_instruments
```
