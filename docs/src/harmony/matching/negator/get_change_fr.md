# get_change_fr (function)

**Code:**
```python
def get_change_fr(token_texts_lower: list) -> dict:
    """
    # Team Cheemu: Identify how to change a French sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"toujours", "assez", "vraiment", "très", "beaucoup de", "totalement", "absolumment",
                                "complètement", "plus", "trop de", "plein de",
                                "souvent", "de temps en temps"}:
            return {token_idx: ("replace", "nie")}
        if token_text_lower in {"personne", "jamais", "ni", "rien", "pas", "non", "ne", "n'", "nulle", "aucun",
                                "aucune", "guère"}:
            return {token_idx: ("replace", "")}
    result = {}
    if len(result) > 0:
        return result
    return {0: ("insert_before", "ne pas")}
```

**Explanation:**
**`get_change_fr` – quick‑look at French negation logic**

```python
def get_change_fr(token_texts_lower: list) -> dict:
```

* **Purpose** – Decide how to flip a French sentence from positive to negative (or vice‑versa) by looking at individual words.

* **Input** – `token_texts_lower`: a list of the sentence’s tokens, all lower‑cased.

* **Process**  
  1. Loop over each token (`token_idx`, `token_text_lower`).  
  2. **Positive‑to‑negative**:  
     * If the token is one of the “strong” adverbs/adjectives  
       (`toujours`, `assez`, `vraiment`, …, `souvent`, `de temps en temps`),  
       return a dict that says *replace this token with “nie”* (`{token_idx: ("replace", "nie")}`).
  3. **Negative‑to‑positive**:  
     * If the token is a negation word (`personne`, `jamais`, `ni`, `rien`, `pas`, `non`, `ne`, `n'`, `nulle`, `aucun`, `aucune`, `guère`),  
       return a dict that says *remove this token* (`{token_idx: ("replace", "")}`).
  4. If no token matches, the function falls back to inserting a negation at the start:  
     `return {0: ("insert_before", "ne pas")}`.

* **Return value** – A dictionary mapping a token index to a tuple `(operation, text)` where `operation` is one of `"replace"`, `"insert_before"`, or `"insert_after"`.  
  The calling code uses this map to edit the original string.

* **Note** – The `result` variable is never populated; the early `return` statements always exit before it’s used. The final `if len(result) > 0:` block is effectively dead code.

**Imports:**
```
import re
```
