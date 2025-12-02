# test_single_instrument_simple_2 (function)

**Code:**
```python
def test_single_instrument_simple_2(self):
        instrument = create_instrument_from_list(["question A", "question B", "question C"], [],
                                                 instrument_name="potato")
        self.assertEqual(3, len(instrument.questions))
        self.assertEqual("potato", instrument.instrument_name)
```

**Explanation:**
**Function Explanation: `test_single_instrument_simple_2`**

This function is a unit test case written in Python using the `unittest` framework. It tests the functionality of the `create_instrument_from_list` function.

**What it does:**

1. Creates an instrument with 3 questions using the `create_instrument_from_list` function.
2. Verifies that the instrument has 3 questions (`self.assertEqual(3, len(instrument.questions))`).
3. Verifies that the instrument's name is set to "potato" (`self.assertEqual("potato", instrument.instrument_name)`).

**In simple terms:**

This function checks if the `create_instrument_from_list` function correctly creates an instrument with 3 questions and sets its name to "potato".

**Imports:**
```
import sys, import unittest, from harmony import create_instrument_from_list, import_instrument_into_harmony_web
```
