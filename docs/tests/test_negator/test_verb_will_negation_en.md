# test_verb_will_negation_en (function)

**Code:**
```python
def test_verb_will_negation_en(self):
        text = "I won't feel happy"
        self.assertEqual("I will feel happy", negate(text, "en"))
```

**Explanation:**
**Function Explanation: `test_verb_will_negation_en`**

This function tests the negation of a sentence in English (denoted by "en") where the verb is "will" (e.g., "won't"). The function takes a sentence as input and checks if the output of the `negate` function is correct.

**Step-by-Step Breakdown:**

1. The function sets a sample sentence: "I won't feel happy".
2. It calls the `negate` function with the sentence and language code ("en") as arguments.
3. The expected output is set to: "I will feel happy".
4. The function uses the `self.assertEqual` method to check if the actual output of the `negate` function matches the expected output.

**In Simple Terms:**

This function tests a specific scenario where a sentence in English uses the verb "will" in the negative form ("won't"). It checks if the `negate` function correctly converts this sentence to its positive form ("will").

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
