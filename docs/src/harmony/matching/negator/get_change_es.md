# get_change_es (function)

**Code:**
```python
def get_change_es(token_texts_lower: list) -> dict:
    """
    # Team Cheemu: Identify how to change a Spanish sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"siempre", "bastante", "realmente", "muy", "mucho", "totalmente", "totalmente",
                                "absolutamente",
                                "completamente",
                                "frecuentemente", "frequentemente", "veces"}:
            return {token_idx: ("replace", "nunca")}
        if token_text_lower in {"nunca", "jamás", "ni", "no"}:
            return {token_idx: ("replace", "")}
    result = {}
    if len(result) > 0:
        return result
    return {0: ("insert_before", "no")}
```

**Explanation:**
**`get_change_es` – Spanish “negation helper**  

- **Input**: a list of the sentence’s tokens, all lower‑cased (`token_texts_lower`).  
- **What it does**:  
  1. Walks through the tokens one by one.  
  2. If it finds a *positive* adverb/phrase (e.g., “siempre”, “muy”, “totalmente”, etc.) it returns a dict telling the caller to **replace that token with “nunca”**.  
  3. If it finds a *negative* word (e.g., “nunca”, “jamás”, “ni”, “no”) it returns a dict telling the caller to **remove that token** (replace with an empty string).  
  4. If no such token is found, it falls back to inserting the word “no” **before the first token** (`{0: ("insert_before", "no")}`).

- **Return value**: a dictionary mapping the token index to a tuple `(operation, text)`, where `operation` is one of `"replace"`, `"insert_before"`, or `"insert_after"` (the latter isn’t used here). This dict is later used by `negate()` to actually edit the sentence.

**Imports:**
```
import re
```
