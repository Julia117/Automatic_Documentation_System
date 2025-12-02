# test_unrelated_topic_to_question (function)

**Code:**
```python
def test_unrelated_topic_to_question(self):
        match = match_instruments([self.veg], topics=["apple", "pear", "orange"])
        self.assertTrue(not match.questions[0].topics)
        self.assertTrue(not match.questions[1].topics)
        self.assertTrue(not match.questions[2].topics)
```

**Explanation:**
**Function Explanation: `test_unrelated_topic_to_question`**

This function tests the `match_instruments` function by passing a list of instruments (`self.veg`) and a list of unrelated topics (`["apple", "pear", "orange"]`). The test expects that no topics are matched with the questions in the instrument.

In simpler terms, this function checks that when you try to match a list of questions with topics that are not related to the questions, the function returns no matched topics.

**Imports:**
```
import sys, import unittest, from harmony import match_instruments, from harmony.util.instrument_helper import create_instrument_from_list
```
