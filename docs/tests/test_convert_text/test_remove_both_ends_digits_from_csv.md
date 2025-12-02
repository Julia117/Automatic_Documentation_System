# test_remove_both_ends_digits_from_csv (function)

**Code:**
```python
def test_remove_both_ends_digits_from_csv(self):
        instruments = convert_text_to_instruments(both_ends_digits_csv)
        questions = instruments[0].questions
        self.assertEqual("How are you today", questions[0].question_text)
        self.assertEqual("Are you feeling better", questions[1].question_text)
```

**Explanation:**
**Function Explanation: `test_remove_both_ends_digits_from_csv`**

This function is a unit test case written in Python using the `unittest` framework. Its purpose is to verify that a specific function, `convert_text_to_instruments`, correctly removes digits from both ends of a question text when processing a CSV file.

Here's a step-by-step breakdown:

1. `instruments = convert_text_to_instruments(both_ends_digits_csv)`: This line calls the `convert_text_to_instruments` function, passing a CSV file (`both_ends_digits_csv`) as an argument. The function is expected to return a list of instrument objects.
2. `questions = instruments[0].questions`: This line extracts the list of questions from the first instrument object in the list.
3. `self.assertEqual("How are you today", questions[0].question_text)`: This line asserts that the question text of the first question is equal to the expected value ("How are you today").
4. `self.assertEqual("Are you feeling better", questions[1].question_text)`: This line asserts that the question text of the second question is equal to the expected value ("Are you feeling better").

In summary, this function tests that the `convert_text_to_instruments` function correctly removes digits from both ends of question texts when processing a CSV file with questions like "How are you today 123" and "Are you feeling better 456".

**Imports:**
```
import sys, import unittest, from harmony import convert_text_to_instruments, from harmony.schemas.requests.text import RawFile
```
