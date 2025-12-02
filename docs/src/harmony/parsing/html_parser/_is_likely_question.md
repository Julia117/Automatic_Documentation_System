# _is_likely_question (function)

**Code:**
```python
def _is_likely_question(text: str) -> bool:
    """
    Determine if a text segment is likely to be a questionnaire item.
    
    Uses heuristics to identify potential questionnaire items:
    - Contains question words or patterns
    - Has appropriate length
    - Doesn't look like navigation or metadata
    
    Args:
        text (str): Text segment to evaluate
        
    Returns:
        bool: True if the text is likely a question
    """
    text_lower = text.lower()
    
    # Skip navigation and common non-question patterns
    skip_patterns = [
        'click here', 'read more', 'continue', 'next', 'previous',
        'home', 'about', 'contact', 'privacy', 'terms',
        'copyright', 'all rights reserved', 'menu', 'navigation'
    ]
    
    for pattern in skip_patterns:
        if pattern in text_lower:
            return False
    
    # Look for question indicators
    question_indicators = [
        'how', 'what', 'when', 'where', 'why', 'who', 'which',
        'do you', 'are you', 'have you', 'would you', 'could you',
        'please', 'rate', 'scale', 'agree', 'disagree', 'often',
        'never', 'sometimes', 'always', 'feel', 'think', 'believe'
    ]
    
    # Check for question indicators
    for indicator in question_indicators:
        if indicator in text_lower:
            return True
    
    # Check if it ends with a question mark
    if text.strip().endswith('?'):
        return True
    
    # Check length - typical questionnaire items are of reasonable length
    if 20 <= len(text) <= 200:
        # Additional heuristics for questionnaire-like content
        if any(word in text_lower for word in ['you', 'your', 'i', 'my']):
            return True
    
    return False
```

**Explanation:**
**Function Explanation: `_is_likely_question(text: str) -> bool`**

This function determines whether a given text segment is likely to be a questionnaire item. It uses a set of heuristics to identify potential questionnaire items.

**Heuristics:**

1. **Skip navigation and common non-question patterns**: If the text contains common navigation or metadata patterns (e.g., "click here", "read more"), it's likely not a question.
2. **Look for question indicators**: If the text contains words or phrases that are commonly used in questions (e.g., "how", "what", "when"), it's likely a question.
3. **Check for question mark**: If the text ends with a question mark, it's likely a question.
4. **Check length**: Typical questionnaire items are of reasonable length (20-200 characters). If the text meets this length criterion, it's likely a question.
5. **Additional heuristics for questionnaire-like content**: If the text contains words like "you", "your", "i", or "my", it's likely a question.

**Return Value:**

The function returns `True` if the text is likely a questionnaire item and `False` otherwise.

**Imports:**
```
from typing import List, from harmony.schemas.requests.text import RawFile, Instrument, Question, from harmony.parsing.util import normalise_text
```
