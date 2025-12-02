# test_simple_example_es (function)

**Code:**
```python
def test_simple_example_es(self):
        text = "mi siento deprimido"
        self.assertEqual("no mi siento deprimido", negate(text, "es"))
```

**Explanation:**
**Function Explanation: `test_simple_example_es`**

This function is a test case for a negation function called `negate`. It checks if the negation function correctly negates a given sentence in Spanish.

**Breakdown:**

1. `text = "mi siento deprimido"`: This line sets the input sentence to be negated, which is a Spanish sentence meaning "I feel depressed".
2. `self.assertEqual("no mi siento deprimido", negate(text, "es"))`: This line calls the `negate` function with the input sentence and the language code "es" (Spanish). It then asserts that the output of the `negate` function is equal to the expected negated sentence, which is "no mi siento deprimido" (meaning "I don't feel depressed").

**In simple terms:** This function tests if the `negate` function correctly translates a positive sentence to a negative sentence in Spanish.

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
