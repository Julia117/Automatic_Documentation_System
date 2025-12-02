# _extract_text_basic (function)

**Code:**
```python
def _extract_text_basic(html_content: str) -> str:
    """
    Basic text extraction from HTML without external dependencies.
    
    This is a fallback method that uses simple string operations
    to remove HTML tags when BeautifulSoup is not available.
    
    Args:
        html_content (str): Raw HTML content
        
    Returns:
        str: Extracted text content
    """
    import re
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', html_content)
    
    # Handle common HTML entities
    html_entities = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&apos;': "'",
        '&nbsp;': ' '
    }
    
    for entity, replacement in html_entities.items():
        text = text.replace(entity, replacement)
    
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
```

**Explanation:**
**Function Explanation: `_extract_text_basic`**

This function extracts text from HTML content without using any external libraries like BeautifulSoup. It's a basic text extraction method that uses regular expressions to remove HTML tags and replace common HTML entities.

Here's a step-by-step breakdown:

1. **Remove HTML tags**: It uses a regular expression to replace all HTML tags with a space.
2. **Replace HTML entities**: It replaces common HTML entities like `&amp;` with their corresponding characters.
3. **Clean up whitespace**: It removes multiple whitespace characters and strips any leading or trailing whitespace from the text.

The function takes in raw HTML content as a string and returns the extracted text content as a string.

**Imports:**
```
from typing import List, from harmony.schemas.requests.text import RawFile, Instrument, Question, from harmony.parsing.util import normalise_text
```
