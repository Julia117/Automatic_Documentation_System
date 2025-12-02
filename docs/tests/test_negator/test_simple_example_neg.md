# test_simple_example_neg (function)

**Code:**
```python
def test_simple_example_neg(self):
        text = "I feel depressed"
        print(negate(text, "en"))
        self.assertEqual("never I feel depressed", negate(text, "en"))
```

**Explanation:**
**Function Explanation: `test_simple_example_neg`**

This function is a unit test case written in Python using the `unittest` framework. It tests the functionality of a `negate` function, which is not shown in this code snippet.

**Function Breakdown:**

1. `text = "I feel depressed"`: Assigns a string variable `text` with the value "I feel depressed".
2. `print(negate(text, "en"))`: Calls the `negate` function with the `text` variable and the language code "en" (English). The result is printed to the console.
3. `self.assertEqual("never I feel depressed", negate(text, "en"))`: Asserts that the result of calling `negate` with the `text` variable and language code "en" is equal to the string "never I feel depressed". If the assertion fails, the test will fail.

**In Simple Terms:**

This function tests the `negate` function by passing a sentence "I feel depressed" and checking if the negated sentence "never I feel depressed" is returned. The test will pass if the `negate` function works correctly.

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
