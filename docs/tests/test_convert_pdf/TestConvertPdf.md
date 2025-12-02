# TestConvertPdf (class)

**Code:**
```python
class TestConvertPdf(unittest.TestCase):

    def test_single_instrument(self):
        self.assertEqual(1, len(convert_pdf_to_instruments(pdf_gad_7_2_questions)))

    def test_two_questions(self):
        self.assertEqual(2, len(convert_pdf_to_instruments(pdf_gad_7_2_questions)[0].questions))
```

**Explanation:**
**Class Explanation: `TestConvertPdf`**

This class is a unit test case written in Python using the `unittest` framework. Its purpose is to test the functionality of the `convert_pdf_to_instruments` function.

**In Simple Terms:**

This class contains two test methods:

1. `test_single_instrument`: Tests that the `convert_pdf_to_instruments` function correctly converts a single PDF file (`pdf_gad_7_2_questions`) into an instrument with a single question.
2. `test_two_questions`: Tests that the `convert_pdf_to_instruments` function correctly converts a single PDF file (`pdf_gad_7_2_questions`) into an instrument with two questions.

**Key Points:**

* The class uses the `unittest` framework to write and run unit tests.
* The `convert_pdf_to_instruments` function is being tested, which is assumed to be a function that converts a PDF file into an instrument object.
* The test methods use assertions to verify that the expected output is produced by the `convert_pdf_to_instruments` function.

**Imports:**
```
import sys, import unittest, from harmony import convert_pdf_to_instruments, from harmony.schemas.requests.text import RawFile, from harmony import download_models
```
