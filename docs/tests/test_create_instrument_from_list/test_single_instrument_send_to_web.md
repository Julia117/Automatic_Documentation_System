# test_single_instrument_send_to_web (function)

**Code:**
```python
def test_single_instrument_send_to_web(self):
        instrument = create_instrument_from_list(["question A", "question B"], [])
        web_url = import_instrument_into_harmony_web(instrument)
        self.assertIn("harmonydata.ac.uk", web_url)
```

**Explanation:**
**Function Explanation: `test_single_instrument_send_to_web`**

This function tests the process of sending a single instrument to the Harmony web UI. Here's a step-by-step breakdown:

1. **Create an instrument**: It creates an instrument object using the `create_instrument_from_list` function, passing in a list of questions and an empty list of options.
2. **Import instrument into Harmony web**: It calls the `import_instrument_into_harmony_web` function, passing in the created instrument object. This function serializes the instrument data into a JSON string, encodes it, and constructs a URL to import the instrument into the Harmony web UI.
3. **Verify the URL**: It checks if the constructed URL contains the string "harmonydata.ac.uk", which is the base URL of the Harmony web UI.

In essence, this function ensures that the instrument can be successfully sent to the Harmony web UI and that the resulting URL is correct.

**Imports:**
```
import sys, import unittest, from harmony import create_instrument_from_list, import_instrument_into_harmony_web
```
