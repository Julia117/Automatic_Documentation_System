# clean_question_text (function)

**Code:**
```python
def clean_question_text(question_text):
    question_text = re.sub(r'\s+', ' ', question_text)
    question_text = question_text.strip()
    return question_text
```

**Explanation:**
**Function Explanation: `clean_question_text`**

This function takes a string input (`question_text`) and returns a cleaned version of it.

Here's what it does:

1. **Remove extra whitespace**: It replaces one or more consecutive whitespace characters (`\s+`) with a single space (`' '`).
2. **Strip leading and trailing whitespace**: It removes any leading or trailing whitespace characters from the string using the `strip()` method.
3. **Return the cleaned string**: The function returns the cleaned `question_text` string.

In simple terms, this function removes unnecessary whitespace from a string, making it easier to work with.

**Imports:**
```
import re, import torch, from harmony.parsing.util.tika_wrapper import parse_pdf_to_list, from harmony.schemas.requests.text import RawFile, Instrument, from tqdm import tqdm, from transformers import AutoModelForTokenClassification, AutoTokenizer, import harmony
```
