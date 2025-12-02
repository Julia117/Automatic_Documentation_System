# parse_excel_to_pandas (function)

**Code:**
```python
def parse_excel_to_pandas(this_file_contents: str) -> dict:
    content_type, content_string = this_file_contents.split(",")
    excel_as_byte_array = base64.b64decode(content_string)
    xls_with_all_sheets = pd.ExcelFile(io.BytesIO(excel_as_byte_array))

    response = {}
    for sheet_name in xls_with_all_sheets.sheet_names:
        df = pd.read_excel(io.BytesIO(excel_as_byte_array), sheet_name=sheet_name, header=None)
        response[sheet_name] = df

    return response
```

**Explanation:**
**Function Explanation: `parse_excel_to_pandas`**

This function takes a string containing the contents of an Excel file, encoded in Base64, and returns a dictionary where each key is the name of an Excel sheet and the value is a Pandas DataFrame containing the data from that sheet.

Here's a step-by-step breakdown:

1. The input string is split into two parts: the content type and the Base64-encoded Excel file contents.
2. The Base64-encoded contents are decoded back into a byte array.
3. The byte array is used to create a Pandas ExcelFile object, which allows us to read the Excel file.
4. The function iterates over the names of all sheets in the Excel file.
5. For each sheet, a Pandas DataFrame is created by reading the sheet from the Excel file.
6. The DataFrame is added to the response dictionary with the sheet name as the key.
7. The function returns the response dictionary.

In essence, this function takes a Base64-encoded Excel file and converts it into a dictionary of Pandas DataFrames, one for each sheet in the Excel file.

**Imports:**
```
import base64, import io, import pandas as pd
```
