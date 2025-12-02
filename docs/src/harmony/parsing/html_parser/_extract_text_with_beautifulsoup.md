# _extract_text_with_beautifulsoup (function)

**Code:**
```python
def _extract_text_with_beautifulsoup(html_content: str) -> str:
    """
    Extract text content from HTML using BeautifulSoup.
    
    This provides better text extraction by:
    - Removing script and style tags
    - Preserving semantic structure
    - Handling HTML entities properly
    
    Args:
        html_content (str): Raw HTML content
        
    Returns:
        str: Extracted text content
    """
    try:
        soup = BeautifulSoup(html_content, DEFAULT_PARSER)
        
        # Remove script and style elements
        for element in soup(["script", "style"]):
            element.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except Exception as e:
        # Fall back to basic extraction if BeautifulSoup fails
        return _extract_text_basic(html_content)
```

**Explanation:**
This function, `_extract_text_with_beautifulsoup`, extracts text content from a given HTML string using the BeautifulSoup library. It:

1. Removes script and style tags to prevent them from interfering with the text extraction.
2. Preserves the semantic structure of the HTML by keeping the original order of elements.
3. Handles HTML entities properly, such as converting `&amp;` to `&`.

If BeautifulSoup fails for any reason, it falls back to a basic text extraction method, `_extract_text_basic`, to ensure that some text is still extracted.

The function returns the extracted text content as a string.

**Imports:**
```
from typing import List, from harmony.schemas.requests.text import RawFile, Instrument, Question, from harmony.parsing.util import normalise_text
```
