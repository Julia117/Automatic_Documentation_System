# tokenise (function)

**Code:**
```python
def tokenise(text):
    tokens = list(re_word.finditer(text))

    return tokens
```

**Explanation:**
**`tokenise(text)` – quick word‑tokeniser**

```python
def tokenise(text):
    tokens = list(re_word.finditer(text))
    return tokens
```

- `re_word` is a compiled regular‑expression that matches individual words in a string.  
- `re_word.finditer(text)` scans the whole `text` and yields a match object for every word it finds.  
- `list(...)` turns that iterator into a list, so the function returns a list of match objects (each containing the matched word and its start/end positions).  

In short: it splits the input string into word‑level tokens and returns them as a list of regex match objects.

**Imports:**
```
import re
```
