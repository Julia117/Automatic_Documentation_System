# negate (function)

**Code:**
```python
def negate(text: str, language: str) -> str:
    """
    Converts negative sentences to positive and vice versa.
    Not meant to generate 100% accurate natural language, it's to go into transformer model and is not shown to a human.
    :param text:
    :param language:
    "en" for English, "pt" for Portuguese, "es" for Spanish, "it" for Italian, "de" for German, "fr" for French.
    :return: the sentence negated
    """
    tokens = tokenise(text)
    token_texts = [token.group() for token in tokens]
    token_texts_lower = [token.group().lower() for token in tokens]

    if language == "pt":
        changes = get_change_pt(token_texts_lower)
    elif language == "es":
        changes = get_change_es(token_texts_lower)
    elif language == "it":
        changes = get_change_it(token_texts_lower)
    elif language == "fr":
        changes = get_change_fr(token_texts_lower)
    elif language == "de":
        changes = get_change_de(token_texts_lower)
    else:
        changes = get_change_en(token_texts_lower)

    for token_idx, match in reversed(list(enumerate(tokens))):
        if token_idx in changes:
            change_operation, change_text = changes[token_idx]
            if change_operation == "replace":
                prefix  = text[:match.start()]
                suffix = text[match.end():]
                if prefix.endswith(" ") and suffix.startswith(" ") and change_text  == "":
                    prefix = prefix[:-1]
                text = prefix + change_text + suffix
            elif change_operation == "insert_after":
                prefix = text[:match.end()]
                suffix = text[match.end():]
                if prefix != "" and not prefix.endswith(" "):
                    prefix += " "
                if suffix != "" and not suffix.startswith(" "):
                    suffix = " " + suffix
                text = prefix + change_text + suffix
            elif change_operation == "insert_before":
                prefix = text[:match.start()]
                suffix = text[match.start():]
                if prefix != "" and not prefix.endswith(" "):
                    prefix += " "
                if suffix != "" and not suffix.startswith(" "):
                    suffix = " " + suffix
                text = prefix + change_text + suffix
    return text
```

**Explanation:**
**`negate(text, language)` – quick “flip‑negation” helper**

1. **Tokenise the sentence**  
   ```python
   tokens = tokenise(text)
   ```
   `tokens` is a list of regex match objects for each word/phrase in `text`.  
   Two helper lists are built:
   * `token_texts` – the original token strings  
   * `token_texts_lower` – the same strings, all lower‑cased (used for matching)

2. **Pick the language‑specific rule set**  
   Depending on `language` (`en`, `pt`, `es`, `it`, `de`, `fr`) the function calls the corresponding `get_change_*` helper.  
   Each helper scans the lower‑cased tokens and returns a **dictionary** mapping a token index → a tuple  
   `(operation, replacement_text)` where `operation` is one of:
   * `"replace"` – swap the token for `replacement_text`
   * `"insert_before"` – add `replacement_text` before the token
   * `"insert_after"` – add `replacement_text` after the token

3. **Apply the changes**  
   The loop iterates over the tokens **backwards** (so earlier edits don’t shift later indices).  
   For each token that has an entry in `changes`:
   * **replace** – cut out the token and insert `replacement_text` (handles spacing when the replacement is empty)
   * **insert_after** – insert `replacement_text` after the token, adding spaces if needed
   * **insert_before** – insert `replacement_text` before the token, adding spaces if needed

4. **Return the modified sentence**  
   The final `text` string is the “negated” version (positive → negative or vice‑versa).  
   It’s intentionally simple and not guaranteed to be grammatically perfect; it’s meant to feed a transformer model, not to be shown to a human.

**Imports:**
```
import re
```
