# test_topic_in_question (function)

**Code:**
```python
def test_topic_in_question(self):
        match = match_instruments([self.veg], topics=["potato", "tomato", "radish"])
        self.assertEqual(match.questions[0].topics, ["potato"])
        self.assertEqual(match.questions[1].topics, ["tomato"])
        self.assertEqual(match.questions[2].topics, ["radish"])
```

**Explanation:**
**Function Explanation: `test_topic_in_question`**

This function tests the `match_instruments` function to ensure it correctly matches topics with questions.

**In Simple Terms:**

1. It creates a list of questions (`self.veg`) from a predefined list of strings.
2. It calls the `match_instruments` function with the list of questions and a list of topics (`["potato", "tomato", "radish"]`).
3. It asserts that the first question is related to "potato", the second question is related to "tomato", and the third question is related to "radish".

**Purpose:**

This function ensures that the `match_instruments` function is working correctly by testing its ability to match topics with questions.

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, from harmony.util.instrument_helper import create_instrument_from_list
```
