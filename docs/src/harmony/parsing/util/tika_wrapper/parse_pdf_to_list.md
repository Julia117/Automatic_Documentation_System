# parse_pdf_to_list (function)

**Code:**
```python
def parse_pdf_to_list(contents: str) -> list[str]:
    """
    Call the Tika library (Java, called via a server) to process a PDF file into a list of strings.

    You need to have Tika running locally or on a remote server for this function to work:

    <code>
    java -jar tika-server-standard-2.3.0.jar
    </code>

    :param contents: The base64 encoding of the PDF file
    :return: A str containing the content of the document.
    """
    print("Preparing data for Tika")
    content_type, content_string = contents.split(",")
    file_in_bytes = base64.b64decode(content_string)

    file = io.BytesIO(file_in_bytes)
    print("Calling Tika")
    parsed = parser.from_buffer(file, xmlContent=True, requestOptions={'timeout': 300})
    print("Got response from Tika")
    parsed_xml = parsed["content"]

    et = html.fromstring(parsed_xml)
    pages = et.getchildren()[1].getchildren()
    print("Parsed response from Tika")

    return [str(page.text_content()) for page in pages]
```

**Explanation:**
**Function Explanation: `parse_pdf_to_list`**

This function takes a base64-encoded PDF file as input and uses the Tika library to extract its content. Tika is a Java library that can parse various file formats, including PDF.

Here's a step-by-step breakdown:

1. **Prepare data for Tika**: The function splits the input string into two parts: the content type and the base64-encoded PDF file.
2. **Decode the PDF file**: The function decodes the base64-encoded PDF file into a byte array.
3. **Create a file-like object**: The function creates a file-like object from the decoded byte array.
4. **Call Tika**: The function uses the Tika library to parse the PDF file. It sets the `xmlContent` parameter to `True` to extract the content as XML.
5. **Get the parsed response**: The function retrieves the parsed response from Tika, which contains the extracted content.
6. **Parse the XML response**: The function uses the `html.fromstring` method to parse the XML response into an HTML element tree.
7. **Extract page content**: The function extracts the content from each page of the PDF file by iterating over the children of the HTML element tree.
8. **Return the page content as a list**: The function returns a list of strings, where each string represents the content of a page in the PDF file.

In summary, this function uses Tika to extract the content of a PDF file and returns it as a list of strings, one string per page.

**Imports:**
```
import base64, import io, from lxml import html, from tika import parser
```
