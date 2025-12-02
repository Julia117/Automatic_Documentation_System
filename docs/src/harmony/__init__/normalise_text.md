# normalise_text (function)

**Code:**
```python
def normalise_text(text: str) -> str:
    """
    Normalizes text by removing extra whitespace and converting to lowercase.
    
    Args:
        text (str): The input text to normalize
        
    Returns:
        str: Normalized text
    """
    return ' '.join(text.strip().split()).lower()
```

**Explanation:**
**Normalizing Text Function**

This function takes in a string of text and returns a normalized version of it. Normalization involves:

1. Removing extra whitespace (spaces) from the text.
2. Converting the text to lowercase.

Here's a step-by-step breakdown:

1. `text.strip()`: Removes leading and trailing whitespace from the text.
2. `text.split()`: Splits the text into a list of words, using whitespace as the delimiter.
3. `' '.join(...)`: Joins the list of words back into a single string, with a single space between each word.
4. `.lower()`: Converts the resulting string to lowercase.

The function returns the normalized text as a string.

**Imports:**
```
from typing import List, Optional
```
