# createModel (class)

**Code:**
```python
class createModel:
    def encode(self, sentences, convert_to_numpy=True):
        # Generate a dummy embedding with 768 dimensions for each sentence
        return numpy.array([[1] * 768] * len(sentences))
```

**Explanation:**
**Explanation of the `createModel` class**

The `createModel` class is a simple class that provides a method to encode sentences into numerical vectors. 

Here's a breakdown of the `encode` method:

- It takes two parameters: `sentences` (a list of sentences to be encoded) and `convert_to_numpy` (a boolean flag to convert the output to a NumPy array).
- It generates a dummy embedding with 768 dimensions for each sentence in the input list.
- It returns a 2D NumPy array where each row represents the embedding of a sentence.

In essence, this class is a placeholder for a real model that would typically use a deep learning architecture to generate meaningful embeddings for sentences. However, in this case, it simply returns a dummy embedding with all elements set to 1.

**Imports:**
```
import sys, import unittest, import numpy, from harmony.matching.default_matcher import convert_texts_to_vector
```
