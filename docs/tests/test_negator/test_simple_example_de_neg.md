# test_simple_example_de_neg (function)

**Code:**
```python
def test_simple_example_de_neg(self):
        text = "Ich fühle mich deprimiert"
        self.assertEqual("nicht Ich fühle mich deprimiert", negate(text, "de"))
```

**Explanation:**
**Function Explanation: `test_simple_example_de_neg`**

This function is a test case for a negation function called `negate`. It checks if the negation function correctly negates a given sentence in German.

**Breakdown:**

1. `text = "Ich fühle mich deprimiert"`: This line sets the input sentence to be negated. The sentence is in German and means "I feel depressed".
2. `self.assertEqual("nicht Ich fühle mich deprimiert", negate(text, "de"))`: This line calls the `negate` function with the input sentence and the language code "de" (German). It then asserts that the output of the `negate` function is equal to the expected negated sentence, which is "nicht Ich fühle mich deprimiert" (meaning "not I feel depressed").

**In simple terms:**

This function tests if the `negate` function correctly negates a sentence in German. It checks if the function correctly adds the negation word "nicht" to the original sentence.

**Imports:**
```
import sys, import unittest, from harmony.matching.negator import negate
```
