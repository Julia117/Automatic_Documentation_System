# test_two_instruments_full_metadata (function)

**Code:**
```python
def test_two_instruments_full_metadata(self):
        match_response = match_instruments(
            [instrument_1, instrument_2])
        self.assertEqual(4, len(match_response.questions))
        self.assertEqual(4, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])
```

**Explanation:**
This function, `test_two_instruments_full_metadata`, is a unit test case written in Python. It tests the functionality of the `match_instruments` function, which likely matches and compares two instruments (e.g., questionnaires or surveys) based on their metadata.

Here's a breakdown of what the function does:

1. It calls the `match_instruments` function with two instruments, `instrument_1` and `instrument_2`, as input.
2. It asserts that the `match_response` object returned by `match_instruments` has the following properties:
   - `questions`: a list of 4 questions.
   - `similarity_with_polarity`: a list of 4 similarity scores with their corresponding polarities.
   - The first similarity score is less than 0.99.

In essence, this test case is verifying that when two instruments are matched, the resulting `match_response` object has the expected structure and content.

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, from harmony.schemas.requests.text import Instrument, Question
```
