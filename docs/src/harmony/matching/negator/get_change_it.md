# get_change_it (function)

**Code:**
```python
def get_change_it(token_texts_lower: list) -> dict:
    """
    # Team Cheemu: Identify how to change an Italian sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"sempre", "abbastanza", "realmente", "davvero", "veramente", "molto", "molta", "molti",
                                "molte", "totalmente", "assolutamente",
                                "completamente",
                                "frequentemente", "qualche volta", "a volte", "ogni tanto"}:
            return {token_idx: ("replace", "mai")}
        if token_text_lower in {"mai", "né", "non", "nessuno", "nulla", "niente"}:
            return {token_idx: ("replace", "")}
    result = {}
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"è", "sono", "ero", "erano", "avevano", "avevo", "ho avuto", "sono stato", "sono stata",
                                "sono stati", "siamo stati", "sono state"}:
            result[token_idx] = "insert_before", "non"
    if len(result) > 0:
        return result
    return {0: ("insert_before", "non")}
```

**Explanation:**
**What `get_change_it` does**

`get_change_it` receives a list of the lower‑cased tokens of an Italian sentence and decides *how* to flip the sentence’s polarity (positive ↔ negative).  
It returns a dictionary that maps a token index to a tuple:

```python
{token_index: ("operation", "text_to_use")}
```

* `operation` can be:
  * `"replace"` – replace the token with `text_to_use`
  * `"insert_before"` – insert `text_to_use` just before the token
  * `"insert_after"` – (not used in this function)

**Logic**

1. **Positive → Negative**  
   If the token is a strong positive adverb/phrase (e.g. “sempre”, “molto”, “frequentemente”), the function immediately returns a replacement that turns it into the negative “mai” (“never”).

2. **Negative → Positive**  
   If the token is already a negative word (“mai”, “non”, “nessuno”, etc.), it returns a replacement that removes it (empty string), effectively turning the sentence positive.

3. **Verb‑level negation**  
   If no adverb was found, the function looks for common Italian copular verbs (“è”, “sono”, “ero”, etc.). For each such verb it records an `"insert_before"` operation that will add the word “non” before the verb (e.g., “sono” → “non sono”).

4. **Fallback**  
   If no verb was found either, it defaults to inserting “non” before the very first token, ensuring the sentence is negated.

**Result**

The returned dict is later used by `negate()` to modify the original text accordingly. The function is a simple rule‑based engine that covers the most common polarity switches in Italian.

**Imports:**
```
import re
```
