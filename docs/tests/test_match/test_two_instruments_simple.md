# test_two_instruments_simple (function)

**Code:**
```python
def test_two_instruments_simple(self):
        match_response = match_instruments(
            [instrument_en, instrument_pt])
        self.assertEqual(4, len(match_response.questions))
        self.assertEqual(4, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])
```

**Explanation:**
This function, `test_two_instruments_simple`, is a test case written in Python using the `unittest` framework. It tests the `match_instruments` function, which likely matches two instruments (in this case, `instrument_en` and `instrument_pt`) and returns a response.

Here's a breakdown of what the function does:

1. It calls the `match_instruments` function with two instruments as input.
2. It asserts that the response from `match_instruments` has 4 questions.
3. It asserts that the response from `match_instruments` has 4 similarity values with polarity.
4. It asserts that the first similarity value is less than 0.99.

In simple terms, this function is testing that when two instruments are matched, the response contains 4 questions and 4 similarity values, and the first similarity value is not too high (less than 0.99).

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, from harmony.schemas.requests.text import Instrument, Question
```
