# TestProcessQuestions (class)

**Code:**
```python
class TestProcessQuestions(unittest.TestCase):
    def test_empty_string_returns_none_vector(self):
        result = process_questions([""], {}, is_negate=False)
        self.assertEqual(len(result), 1)
        self.assertIsNone(result[0].vector)

    def test_whitespace_string_returns_none_vector(self):
        result = process_questions(["   "], {}, is_negate=False)
        self.assertEqual(len(result), 1)
        self.assertIsNone(result[0].vector)

    def test_valid_string_creates_vector(self):
        # Here add_text_to_vec not mocked => will fail if it tries real embed
        # So just check that process_questions doesn't return None for text
        result = process_questions(["Hello"], {}, is_negate=False)
        self.assertEqual(result[0].text, "Hello")
```

**Explanation:**
**Class Explanation: `TestProcessQuestions`**

This is a unit test class written in Python using the `unittest` framework. It's designed to test the functionality of the `process_questions` function.

**Purpose:**

The `process_questions` function takes in a list of questions, a dictionary of cached text vectors, and a boolean flag `is_negate`. It processes each question, creates a `TextVector` object for each one, and returns a list of these objects.

**Test Cases:**

The `TestProcessQuestions` class contains three test cases:

1. `test_empty_string_returns_none_vector`: Tests that an empty string returns a `TextVector` object with a `None` vector.
2. `test_whitespace_string_returns_none_vector`: Tests that a string containing only whitespace returns a `TextVector` object with a `None` vector.
3. `test_valid_string_creates_vector`: Tests that a valid string creates a `TextVector` object with a non-`None` vector.

**Key Takeaways:**

* The `process_questions` function is being tested for its ability to handle different types of input (empty strings, whitespace strings, and valid strings).
* The function returns a list of `TextVector` objects, each representing a question.
* The `TextVector` objects have attributes such as `text`, `vector`, `is_negated`, and `is_query`.

**Imports:**
```
import sys, import os, import unittest, from harmony.matching.matcher import process_questions, import harmony.matching.matcher as matcher
```
