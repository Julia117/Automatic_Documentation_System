# test_simple_example_pt (function)

**Code:**
```python
def test_simple_example_pt(self):
        text = "eu me sinto deprimido"
        self.assertEqual("não eu me sinto deprimido", negate(text, "pt"))
```

**Explanation:**
**Function Explanation: `test_simple_example_pt`**

This function is a unit test case written in Python using the `unittest` framework. It tests the functionality of the `negate` function, which is not shown in this code snippet.

**Function Breakdown:**

1. `text = "eu me sinto deprimido"`: This line sets a sample Portuguese text to be negated.
2. `self.assertEqual("não eu me sinto deprimido", negate(text, "pt"))`: This line calls the `negate` function with the sample text and the language code "pt" (for Portuguese). The expected result is then compared to the actual result using the `assertEqual` method.

**In Simple Terms:**

This function tests the negation of a Portuguese sentence. It checks if the `negate` function correctly negates the sentence "eu me sinto deprimido" (I feel depressed) to "não eu me sinto deprimido" (not I feel depressed).

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
