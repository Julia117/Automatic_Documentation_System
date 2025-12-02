# InstrumentToInstrumentSimilarity (class)

**Code:**
```python
class InstrumentToInstrumentSimilarity(BaseModel):
    """
    Defines a similarity relationship on instrument level. The instruments are not contained within this object, because that would make the response object too verbose,
    but their IDs (zero indexed) are included which correspond to their positions in the original list object.
    """
    instrument_1_idx: int = Field(
        description="The index of the first instrument in the similarity pair in the list of instruments passed to Harmony (zero-indexed)")
    instrument_2_idx: int = Field(
        description="The index of the second instrument in the similarity pair in the list of instruments passed to Harmony (zero-indexed)")
    instrument_1_name: str = Field(description="The name of the first instrument in the similarity pai")
    instrument_2_name: str = Field(description="The name of the second instrument in the similarity pai")
    precision: float = Field(description="The precision score of the match between Instrument 1 and Instrument 2")
    recall: float = Field(description="The recall score of the match between Instrument 1 and Instrument 2")
    f1: float = Field(description="The F1 score of the match between Instrument 1 and Instrument 2")
```

**Explanation:**
**InstrumentToInstrumentSimilarity**  
A lightweight Pydantic model that records how similar two instruments are.  
* **instrument_1_idx / instrument_2_idx** – zero‑based positions of the two instruments in the original list you passed to Harmony.  
* **instrument_1_name / instrument_2_name** – human‑readable names of those instruments.  
* **precision, recall, f1** – the standard evaluation metrics computed from the item‑to‑item similarity matrix (higher is better).  

The model does **not** store the full instrument objects, keeping the API response small while still letting you identify which instruments were compared.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
