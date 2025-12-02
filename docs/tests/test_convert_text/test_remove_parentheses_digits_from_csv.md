# test_remove_parentheses_digits_from_csv (function)

**Code:**
```python
def test_remove_parentheses_digits_from_csv(self):
        instruments = convert_text_to_instruments(parentheses_digits_csv)
        questions = instruments[0].questions
        self.assertEqual("I feel tired", questions[0].question_text)
        self.assertEqual("I feel weak", questions[1].question_text)
```

**Explanation:**
**Function Explanation: `test_remove_parentheses_digits_from_csv`**

This function is a unit test case written in Python using the `unittest` framework. Its purpose is to verify that a specific function, `convert_text_to_instruments`, correctly removes parentheses and digits from a CSV file.

Here's a step-by-step breakdown:

1. `instruments = convert_text_to_instruments(parentheses_digits_csv)`: This line calls the `convert_text_to_instruments` function, passing a CSV file named `parentheses_digits_csv` as an argument. The function is expected to return a list of instrument objects.
2. `questions = instruments[0].questions`: This line extracts the list of questions from the first instrument object in the list.
3. `self.assertEqual("I feel tired", questions[0].question_text)`: This line asserts that the question text of the first question is equal to `"I feel tired"`.
4. `self.assertEqual("I feel weak", questions[1].question_text)`: This line asserts that the question text of the second question is equal to `"I feel weak"`.

In simple terms, this function is testing that the `convert_text_to_instruments` function correctly removes parentheses and digits from a CSV file, resulting in the expected question texts.

**Imports:**
```
import sys, import unittest, from harmony import convert_text_to_instruments, from harmony.schemas.requests.text import RawFile
```
