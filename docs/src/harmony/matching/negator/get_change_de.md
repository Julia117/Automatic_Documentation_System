# get_change_de (function)

**Code:**
```python
def get_change_de(token_texts_lower: list) -> dict:
    """
    # Team Cheemu: Identify how to change a German sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"immer", "ziemlich", "wirklich", "sehr", "viel", "total", "absolut",
                                "vollständig",
                                "häufig", "manchmal"}:
            return {token_idx: ("replace", "nie")}
        if token_text_lower in {"nie", "niemals", "weder", "nicht"}:
            return {token_idx: ("replace", "")}
    result = {}
    if len(result) > 0:
        return result
    return {0: ("insert_before", "nicht")}
```

**Explanation:**
**`get_change_de` – quick‑look at German negation logic**

```python
def get_change_de(token_texts_lower: list) -> dict:
```

* **Purpose** – Decide how to flip a German sentence from positive to negative (or vice‑versa) by looking at individual words.

* **How it works**  
  1. Iterate over the lower‑cased tokens (`token_texts_lower`) with their index.  
  2. If a token is one of the *positive‑intensity* words  
     (`immer`, `ziemlich`, `wirklich`, `sehr`, `viel`, `total`, `absolut`, `vollständig`, `häufig`, `manchmal`)  
     → return a dict that says: *replace this token with `"nie"`* (German for “never”).  
  3. If a token is already a negative word (`nie`, `niemals`, `weder`, `nicht`)  
     → return a dict that says: *replace this token with an empty string* (i.e., delete it).  
  4. If none of the above matches, fall back to inserting the word `"nicht"` before the first token:  
     `return {0: ("insert_before", "nicht")}`.

* **Return value** – A mapping `{token_index: (operation, text)}` that the caller uses to modify the original sentence.  
  * `operation` can be `"replace"`, `"insert_before"`, or `"insert_after"`.  
  * `text` is the string to use for that operation.

* **Note** – The `result` variable is unused; the function always returns either a replacement or an insertion.

**Imports:**
```
import re
```
