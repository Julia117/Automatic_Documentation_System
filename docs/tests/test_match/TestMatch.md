# TestMatch (class)

**Code:**
```python
class TestMatch(unittest.TestCase):

    def test_single_instrument_simple(self):
        match_response = match_instruments([instrument_en])
        self.assertEqual(2, len(match_response.questions))
        self.assertEqual(2, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])
        self.assertGreater(0.95, match_response.similarity_with_polarity[0][1])
        self.assertLess(0.99, match_response.similarity_with_polarity[1][1])
        self.assertGreater(0.95, match_response.similarity_with_polarity[1][0])

    def test_two_instruments_simple(self):
        match_response = match_instruments(
            [instrument_en, instrument_pt])
        self.assertEqual(4, len(match_response.questions))
        self.assertEqual(4, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])

    def test_single_instrument_full_metadata(self):
        match_response = match_instruments([instrument_1])
        self.assertEqual(2, len(match_response.questions))
        self.assertEqual(2, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])
        self.assertGreater(0.95, match_response.similarity_with_polarity[0][1])
        self.assertLess(0.99, match_response.similarity_with_polarity[1][1])
        self.assertGreater(0.95, match_response.similarity_with_polarity[1][0])

    def test_two_instruments_full_metadata(self):
        match_response = match_instruments(
            [instrument_1, instrument_2])
        self.assertEqual(4, len(match_response.questions))
        self.assertEqual(4, len(match_response.similarity_with_polarity))
        self.assertLess(0.99, match_response.similarity_with_polarity[0][0])
```

**Explanation:**
**Class Explanation:**

This class, `TestMatch`, is a unit test case written in Python using the `unittest` framework. It's designed to test the functionality of the `match_instruments` function, which is not shown in this code snippet.

**Purpose:**

The purpose of this class is to verify that the `match_instruments` function behaves as expected in different scenarios. It tests the function with various inputs, such as single and multiple instruments, with and without full metadata.

**Test Cases:**

The class contains four test cases:

1. `test_single_instrument_simple`: Tests the function with a single instrument and basic metadata.
2. `test_two_instruments_simple`: Tests the function with two instruments and basic metadata.
3. `test_single_instrument_full_metadata`: Tests the function with a single instrument and full metadata.
4. `test_two_instruments_full_metadata`: Tests the function with two instruments and full metadata.

**Assertions:**

Each test case contains assertions to verify that the `match_instruments` function returns the expected results. These assertions check the length of the `questions` and `similarity_with_polarity` lists, as well as the values within these lists.

**Context:**

The `match_instruments` function is likely used to match instruments (e.g., questionnaires or surveys) based on their metadata. The function returns a `match_response` object, which contains information about the matched instruments, including questions and similarity scores.

**Conclusion:**

In summary, this class is a set of unit tests designed to verify the functionality of the `match_instruments` function. It tests the function with various inputs and assertions to ensure it behaves as expected.

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, from harmony.schemas.requests.text import Instrument, Question
```
