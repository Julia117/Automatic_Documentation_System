# DummyTextVector (class)

**Code:**
```python
class DummyTextVector:
    def __init__(self, text, vector=None, is_negated=False, is_query=False):
        self.text = text
        self.vector = vector
        self.is_negated = is_negated
        self.is_query = is_query
```

**Explanation:**
**DummyTextVector Class Explanation**

The `DummyTextVector` class is a simple data container that holds information about a text. It has four attributes:

1. `text`: The actual text being represented.
2. `vector`: A numerical representation of the text (e.g., a vector in a high-dimensional space).
3. `is_negated`: A boolean indicating whether the text is negated (i.e., its opposite).
4. `is_query`: A boolean indicating whether the text is a query (i.e., a question).

This class is likely used as a placeholder or a mock object in a larger system, where the actual text representation and negation logic are not yet implemented.

**Imports:**
```
import sys, import os, import unittest, from harmony.matching.matcher import process_questions, import harmony.matching.matcher as matcher
```
