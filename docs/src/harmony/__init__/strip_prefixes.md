# strip_prefixes (function)

**Code:**
```python
def strip_prefixes(question: str, prefixes: Optional[List[str]] = None) -> str:
    """
    Strips specified prefixes from a question string if they are present.
    Args:
        question (str): The question string from which prefixes need to be removed.
        prefixes (Optional[List[str]]): A list of prefixes to remove from the question.
                                        If not provided, a default set of common prefixes is used.
    Returns:
        str: The question string with the prefix removed, if a match is found;
             otherwise, the original question.
    Example:
        question = "Have you ever traveled abroad?"
        result = strip_prefixes(question)
        # result -> "traveled abroad?"
    """
    default_prefixes = [
        "Have you ever",
        "Did you ever",
        "Do you",
        "Is it true that",
        "Would you say",
        "Can you",
        "Are you aware that",
        "Do you think",
    ]
    prefixes = prefixes or default_prefixes
    for prefix in prefixes:
        if question.lower().startswith(prefix.lower()):
            return question[len(prefix) :].strip()
    return question
```

**Explanation:**
**Function Explanation: `strip_prefixes`**

This function removes specified prefixes from a question string. It takes two arguments:

1. `question`: The question string from which prefixes need to be removed.
2. `prefixes`: An optional list of prefixes to remove from the question. If not provided, a default set of common prefixes is used.

Here's a step-by-step breakdown:

1. If `prefixes` is not provided, it defaults to a list of common prefixes.
2. The function iterates through each prefix in the list.
3. For each prefix, it checks if the question string starts with the prefix (case-insensitive).
4. If a match is found, it returns the question string with the prefix removed (using slicing).
5. If no match is found, it returns the original question string.

In simple terms, this function helps to remove unnecessary words or phrases from the beginning of a question, making it more concise and readable.

**Imports:**
```
from typing import List, Optional
```
