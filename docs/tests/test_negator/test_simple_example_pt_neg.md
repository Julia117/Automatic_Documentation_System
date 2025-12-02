# test_simple_example_pt_neg (function)

**Code:**
```python
def test_simple_example_pt_neg(self):
        text = "não eu me sinto deprimido"
        self.assertEqual(" eu me sinto deprimido", negate(text, "pt"))
```

**Explanation:**
**Function Explanation: `test_simple_example_pt_neg`**

This function is a test case for a negation function called `negate`. It checks if the negation function correctly negates a sentence in Portuguese.

**Breakdown:**

1. `text = "não eu me sinto deprimido"`: This line sets the input sentence to be negated. The sentence is in Portuguese and means "I don't feel depressed".
2. `self.assertEqual(" eu me sinto deprimido", negate(text, "pt"))`: This line calls the `negate` function with the input sentence and the language code "pt" (for Portuguese). It then asserts that the output of the `negate` function is equal to the expected output, which is the original sentence without the negation (" eu me siento deprimido").

**In simple terms:**

This function tests if the `negate` function can correctly remove the negation from a sentence in Portuguese. If the function works correctly, it should return the original sentence without the negation.

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
