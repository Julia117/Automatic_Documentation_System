# get_change_pt (function)

**Code:**
```python
def get_change_pt(token_texts_lower: list) -> dict:
    """
    Identify how to change a Portuguese sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"sempre", "bastante", "realmente", "muito", "totalmente", "totalmente", "absolutamente",
                                "completamente",
                                "frequentemente", "frequentemente", "vezes", "geralmente", "geralmente"}:
            return {token_idx: ("replace", "nunca")}
        if token_text_lower in {"nunca", "jamais", "nem", "não"}:
            return {token_idx: ("replace", "")}
    result = {}
    if len(result) > 0:
        return result
    return {0: ("insert_before", "não")}
```

**Explanation:**
**`get_change_pt` – quick‑look at Portuguese negation**

```python
def get_change_pt(token_texts_lower: list) -> dict:
```

* **Purpose** – Decide how to flip a Portuguese sentence from positive to negative (or vice‑versa) by looking at individual words.

* **Input** – `token_texts_lower`: a list of the sentence’s tokens, all lower‑cased.

* **Logic**  
  1. Loop over each token (`token_idx`, `token_text_lower`).  
  2. **Positive → Negative**  
     * If the token is one of the “always/very” words  
       (`sempre`, `bastante`, `realmente`, `muito`, `totalmente`, `absolutamente`, `completamente`, `frequentemente`, `vezes`, `geralmente`),  
       return a dict that says: *replace this token with `"nunca"`*.
  3. **Negative → Positive**  
     * If the token is a negation word (`nunca`, `jamais`, `nem`, `não`),  
       return a dict that says: *replace this token with an empty string* (i.e., delete it).
  4. If no token matched, the function falls back to inserting a negation at the start:  
     `return {0: ("insert_before", "não")}`.

* **Return value** – A dictionary mapping the token index to a tuple  
  `(operation, text)` where `operation` is `"replace"`, `"insert_before"`, or `"insert_after"` and `text` is the string to use.

* **Note** – The `result` variable is never populated; the early `return` statements always exit the function, so the final `if len(result) > 0:` block is dead code. The function simply returns the first applicable rule or a default insertion.

**Imports:**
```
import re
```
