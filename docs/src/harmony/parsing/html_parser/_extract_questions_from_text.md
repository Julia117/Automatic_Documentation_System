# _extract_questions_from_text (function)

**Code:**
```python
def _extract_questions_from_text(text: str) -> List[Question]:
    """
    Extract potential questions from text content.
    
    This function looks for question-like patterns in the text and
    creates Question objects from them. It uses heuristics to identify
    sentences that might be questionnaire items.
    
    Args:
        text (str): Extracted text content
        
    Returns:
        List[Question]: List of identified questions
    """
    questions = []
    
    # Normalize the text
    normalized_text = normalise_text(text)
    
    # Split into sentences/lines for potential questions
    # Use multiple delimiters to split the text
    import re
    sentences = re.split(r'[.!?\n\r]+', normalized_text)
    
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        
        # Skip very short or empty sentences
        if len(sentence) < 10:
            continue
            
        # Skip sentences that are likely not questions
        if _is_likely_question(sentence):
            question = Question(
                question_no=str(i + 1),
                question_intro="",
                question_text=sentence,
                options=None,
                source_page=1
            )
            questions.append(question)
    
    return questions
```

**Explanation:**
**Function Explanation: `_extract_questions_from_text`**

This function takes a string of text as input and attempts to extract potential questions from it. It uses heuristics to identify sentences that might be questionnaire items.

Here's a step-by-step breakdown:

1. **Text Normalization**: The input text is normalized to remove any unnecessary characters.
2. **Sentence Splitting**: The normalized text is split into individual sentences using multiple delimiters (e.g., `.`, `!`, `?`, `\n`, `\r`).
3. **Sentence Filtering**: Each sentence is checked to see if it's likely a question. If it's too short (less than 10 characters) or doesn't match the question pattern, it's skipped.
4. **Question Creation**: If a sentence is deemed a potential question, a `Question` object is created with the sentence as its text.
5. **Question List**: The created `Question` objects are added to a list, which is returned as the result.

In essence, this function tries to identify sentences that resemble questions and returns a list of potential questions.

**Imports:**
```
from typing import List, from harmony.schemas.requests.text import RawFile, Instrument, Question, from harmony.parsing.util import normalise_text
```
