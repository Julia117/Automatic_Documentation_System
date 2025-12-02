# test_two_questions (function)

**Code:**
```python
def test_two_questions(self):
        self.assertEqual(2, len(convert_excel_to_instruments(xlsx_gad_7_2_questions)[0].questions))
```

**Explanation:**
**Function Explanation: `test_two_questions`**

This function is a unit test that checks if the `convert_excel_to_instruments` function correctly converts an Excel file (`xlsx_gad_7_2_questions`) into an instrument with exactly 2 questions.

In simpler terms, it's verifying that when you take an Excel file, convert it into an instrument, and then look at the questions within that instrument, there are indeed 2 questions.

**Imports:**
```
import sys, import unittest, from harmony import convert_excel_to_instruments, from harmony.schemas.requests.text import RawFile
```
