# _get_instruments_from_file (function)

**Code:**
```python
def _get_instruments_from_file(file):
    """
    Route files to appropriate parsers based on file type.
    
    Args:
        file: RawFile object containing file content and metadata
        
    Returns:
        List[Instrument]: Parsed instruments from the file
    """
    if file.file_type == FileType.pdf or file.file_type == FileType.docx:
        instruments_from_this_file = convert_pdf_to_instruments(file)
    elif file.file_type == FileType.txt or file.file_type == FileType.csv:
        instruments_from_this_file = convert_text_to_instruments(file)
    elif file.file_type == FileType.xlsx:
        instruments_from_this_file = convert_excel_to_instruments(file)
    elif file.file_type == FileType.html or file.file_type == FileType.htm:
        instruments_from_this_file = convert_html_to_instruments(file)
    else:
        instruments_from_this_file = []
    return instruments_from_this_file
```

**Explanation:**
This function, `_get_instruments_from_file`, takes a `RawFile` object as input and determines which parser to use based on the file type. It then calls the corresponding parser function to parse the file and returns a list of `Instrument` objects.

In simple terms, it acts as a router to direct files to the correct parser based on their type.

**Imports:**
```
from typing import List, from harmony.parsing.excel_parser import convert_excel_to_instruments, from harmony.parsing.pdf_parser import convert_pdf_to_instruments, from harmony.parsing.text_parser import convert_text_to_instruments, from harmony.parsing.html_parser import convert_html_to_instruments, from harmony.schemas.enums.file_types import FileType, from harmony.schemas.requests.text import RawFile, Instrument
```
