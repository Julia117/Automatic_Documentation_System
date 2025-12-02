# test_convert_texts_to_vector_with_batching (function)

**Code:**
```python
def test_convert_texts_to_vector_with_batching(self):
        # Create a list of 10 dummy texts
        texts = ["text" + str(i) for i in range(10)]

        batch_size = 5
        max_batches = 2
        embeddings = convert_texts_to_vector(texts, batch_size=batch_size, max_batches=max_batches)

        self.assertEqual(embeddings.shape[0], 10)

        self.assertEqual(embeddings.shape[1], 384)
```

**Explanation:**
**Function Explanation: `test_convert_texts_to_vector_with_batching`**

This function is a unit test case written in Python using the `unittest` framework. It tests the functionality of the `convert_texts_to_vector` function, which converts a list of text inputs into numerical vector representations.

Here's a simplified breakdown:

1. **Create dummy texts**: A list of 10 dummy texts is created by concatenating "text" with numbers from 0 to 9.
2. **Set batch size and max batches**: The batch size is set to 5, and the maximum number of batches is set to 2.
3. **Call `convert_texts_to_vector` function**: The `convert_texts_to_vector` function is called with the dummy texts, batch size, and max batches as arguments.
4. **Assert expected output shape**: The function asserts that the output shape of the `convert_texts_to_vector` function has 10 rows (one for each text) and 384 columns (the expected dimensionality of the vector representations).

In essence, this test case ensures that the `convert_texts_to_vector` function correctly converts a list of texts into vector representations, with batching enabled.

**Imports:**
```
import sys, import unittest, import numpy, from harmony.matching.default_matcher import convert_texts_to_vector
```
