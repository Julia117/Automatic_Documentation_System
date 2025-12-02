# convert_html_to_instruments (function)

**Code:**
```python
def convert_html_to_instruments(file: RawFile) -> List[Instrument]:
    """
    Convert HTML file to Harmony instruments by extracting text content.
    
    This function parses HTML files and extracts meaningful text content,
    attempting to preserve semantic structure while removing HTML tags.
    Uses BeautifulSoup if available for better parsing, otherwise falls
    back to basic text extraction.
    
    Args:
        file (RawFile): The raw HTML file to parse
        
    Returns:
        List[Instrument]: List of instruments extracted from the HTML
    """
    
    if not file.content:
        return []
    
    # Extract text content from HTML
    if BEAUTIFULSOUP_AVAILABLE:
        text_content = _extract_text_with_beautifulsoup(file.content)
    else:
        text_content = _extract_text_basic(file.content)
    
    if not text_content.strip():
        return []
    
    # Create questions from extracted text
    questions = _extract_questions_from_text(text_content)
    
    if not questions:
        return []
    
    # Create instrument
    instrument = Instrument(
        file_id=file.file_id,
        instrument_name=file.file_name or "HTML Document",
        questions=questions,
        language="en"  # Default to English, could be enhanced with language detection
    )
    
    return [instrument]
```

**Explanation:**
**Function Explanation: `convert_html_to_instruments`**

This function takes an HTML file as input and extracts meaningful text content from it. It then uses this text to create a list of instruments, which are essentially questionnaires.

Here's a step-by-step breakdown:

1. **Check if the file is empty**: If the file has no content, return an empty list.
2. **Extract text content from HTML**: Use BeautifulSoup (if available) or basic text extraction to remove HTML tags and extract the text content.
3. **Create questions from extracted text**: Use the extracted text to identify potential questions and create a list of Question objects.
4. **Create an instrument**: Use the extracted questions to create an Instrument object, which represents a questionnaire.
5. **Return the instrument**: Return a list containing the created Instrument object.

In simple terms, this function takes an HTML file, extracts the text content, identifies potential questions, and creates a questionnaire (Instrument) from it.

**Imports:**
```
from typing import List, from harmony.schemas.requests.text import RawFile, Instrument, Question, from harmony.parsing.util import normalise_text
```
