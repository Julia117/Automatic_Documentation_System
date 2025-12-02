# import_instrument_into_harmony_web (function)

**Code:**
```python
def import_instrument_into_harmony_web(instrument: Instrument, harmony_fe_base_url="https://harmonydata.ac.uk") -> str:
    """
    Import a single instrument into the Harmony web UI.
    @param instrument: An instrument object created by Harmony
    @param harmony_fe_base_url: The base URL of the React app front end, defaulting to the web Harmony front end at harmonydata.ac.uk
    @return: a URL which you can click which will take you to the browser.
    """
    instrument_serialised_as_json = json.dumps(instrument.model_dump())
    instrument_json_b64_encoded_bytes = base64.urlsafe_b64encode(instrument_serialised_as_json.encode('utf-8'))
    instrument_json_b64_encoded_str = instrument_json_b64_encoded_bytes.decode("utf-8")

    url = f"{harmony_fe_base_url}/app/#/import/{instrument_json_b64_encoded_str}"

    return url
```

**Explanation:**
**What it does**

`import_instrument_into_harmony_web` turns a single `Instrument` object into a link that can be opened in the Harmony web UI.

**Step‑by‑step**

1. **Serialize the instrument** – `instrument.model_dump()` creates a plain Python dict from the Pydantic model, then `json.dumps` turns that dict into a JSON string.
2. **Encode the JSON** – The JSON string is UTF‑8 encoded, then base64‑URL‑safe encoded so it can safely travel in a URL.
3. **Build the URL** – The encoded string is appended to the front‑end base URL (`https://harmonydata.ac.uk` by default) in the pattern  
   `…/app/#/import/<encoded‑json>`.
4. **Return the URL** – The function returns this full URL; clicking it will open the Harmony UI and pre‑load the instrument.

**Why it’s useful**

Instead of uploading a file, you can share a single clickable link that instantly loads the instrument into the web interface.

**Imports:**
```
import base64, import json, import uuid, from harmony.schemas.requests.text import Instrument, Question
```
