# get_change_en (function)

**Code:**
```python
def get_change_en(token_texts_lower: list) -> dict:
    """
    Identify how to change an English sentence from positive to negative or vice versa.
    :param doc:
    :return:
    """
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"always", "rather", "really", "very", "totally", "utterly", "absolutely", "completely",
                                "frequently", "often", "sometimes", "generally", "usually"}:
            return {token_idx: ("replace", "never")}
        # Team Cheemu: added these if statements to handle negative contractions (eg. can't, won't, shan't)
        if token_text_lower == "can't":
            return {token_idx: ("replace", "can")}
        if token_text_lower == "won't":
            return {token_idx: ("replace", "will")}
        if token_text_lower == "shan't":
            return {token_idx: ("replace", "shall")}
        if token_text_lower in {"never", "not", "don't"}:
            return {token_idx: ("replace", "")}
        if token_text_lower in {"cannot"}:
            return {token_idx: ("replace", "can")}
    result = {}
    for token_idx, token_text_lower in enumerate(token_texts_lower):
        if token_text_lower in {"is", "are", "am", "are", "was", "were", "has", "have", "had"}:
            result[token_idx] = "insert_after", "not"
    if len(result) > 0:
        return result
    #     print ("fallback", doc)
    return {0: ("insert_before", "never")}
```

**Explanation:**
**`get_change_en` – quick‑look at how we flip an English sentence**

| What it does | How it works |
|--------------|--------------|
| **Input** – a list of the sentence’s tokens, all lower‑cased (`token_texts_lower`). | The function walks through the list once. |
| **Goal** – decide *one* change that will turn a positive sentence into a negative one (or vice‑versa). | It returns a dictionary: `{token_index: (operation, replacement_text)}`. |
| **Operations** | 1. **replace** – swap the token for another word (or delete it).  <br>2. **insert_after** – add a word right after the token.  <br>3. **insert_before** – add a word right before the token. |
| **Step‑by‑step** | 1. **Intensity words** (`always`, `really`, `very`, …) → replace with **“never”**.  <br>2. **Negative contractions**: <br> • `can't` → `can`  <br> • `won’t` → `will`  <br> • `shan’t` → `shall`  <br>3. **Existing negations** (`never`, `not`, `don’t`) → delete the word (replace with empty string).  <br>4. **`cannot`** → `can`.  <br>5. If none of the above matched, look for auxiliary verbs (`is`, `are`, `am`, `was`, `were`, `has`, `have`, `had`).  For each, **insert “not” after it**.  <br>6. If still nothing matched, **fallback**: insert “never” before the first token. |
| **Return value** | A single‑entry dictionary that tells the caller *exactly* which token to touch and how. The caller (the `negate` function) then applies that change to the original text. |

In short:  
*Scan the tokens for a word that signals a change, decide whether to replace it, delete it, or add “not” after an auxiliary, and if nothing fits, prepend “never”. The result is a minimal edit that flips the sentence’s polarity.*

**Imports:**
```
import re
```
