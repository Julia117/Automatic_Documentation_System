# remove_numbers (function)

**Code:**
```python
def remove_numbers(question_text):
    # remove formatted numbers from start of text
    cleaned_text = re.sub(r'^[\s\(]*\d+[\s\.\)\-]*', '', question_text)

    # remove formatted numbers from end of text
    cleaned_text = re.sub(r'[\s\(]*\d+[\s\.\)\-]*$', '', cleaned_text)

    return cleaned_text.strip()
```

**Explanation:**
**Function Explanation: `remove_numbers(question_text)`**

This function removes formatted numbers from the start and end of a given text string, `question_text`. It uses regular expressions to identify and remove numbers that are surrounded by whitespace, parentheses, dots, or hyphens.

Here's a step-by-step breakdown:

1. It removes numbers from the **start** of the text using a regular expression that matches one or more whitespace characters, parentheses, or dots followed by one or more digits and then more whitespace characters, parentheses, or dots.
2. It removes numbers from the **end** of the text using a similar regular expression, but this time it matches numbers at the end of the string.
3. Finally, it returns the cleaned text after removing any leading or trailing whitespace using the `strip()` method.

This function is likely used to preprocess text data, such as question texts, to remove unwanted numbers that may be present at the start or end of the text.

**Imports:**
```
import re, import traceback, from io import StringIO, from typing import List, import pandas as pd, from langdetect import detect, from harmony.schemas.enums.file_types import FileType, from harmony.schemas.requests.text import RawFile, Instrument, Question
```
