# convert_files_to_instruments (function)

**Code:**
```python
def convert_files_to_instruments(files: List[RawFile]) -> List[Instrument]:
    """Convert files to instruments"""
    instruments = []
    for file in files:
        instruments_from_this_file = _get_instruments_from_file(file)
        instruments.extend(instruments_from_this_file)
    return instruments
```

**Explanation:**
This function takes a list of `RawFile` objects, processes each file, and returns a list of `Instrument` objects.

Here's a step-by-step breakdown:

1. It initializes an empty list `instruments` to store the processed `Instrument` objects.
2. It loops through each `RawFile` object in the input list `files`.
3. For each `RawFile` object, it calls the `_get_instruments_from_file` function to process the file and extract `Instrument` objects.
4. The extracted `Instrument` objects are added to the `instruments` list.
5. Finally, it returns the complete list of `Instrument` objects.

In essence, this function acts as a file converter, taking raw files as input and producing a list of processed instruments as output.

**Imports:**
```
from typing import List, from harmony.parsing.excel_parser import convert_excel_to_instruments, from harmony.parsing.pdf_parser import convert_pdf_to_instruments, from harmony.parsing.text_parser import convert_text_to_instruments, from harmony.parsing.html_parser import convert_html_to_instruments, from harmony.schemas.enums.file_types import FileType, from harmony.schemas.requests.text import RawFile, Instrument
```
