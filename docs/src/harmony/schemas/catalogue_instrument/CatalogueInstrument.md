# CatalogueInstrument (class)

**Code:**
```python
class CatalogueInstrument(BaseModel):
    instrument_name: str = Field(description="Instrument name")
    instrument_url: str = Field(description="Instrument URL")
    source: str = Field(description="Source")
    sweep: str = Field(description="Sweep")
    metadata: dict = Field(default=None, description="Metadata")
```

**Explanation:**
**CatalogueInstrument** – a lightweight Pydantic model that represents a single instrument entry in the catalogue.

| Field | Type | Purpose |
|-------|------|---------|
| `instrument_name` | `str` | Human‑readable name of the instrument. |
| `instrument_url` | `str` | Link to the instrument’s online location. |
| `source` | `str` | Origin or publisher of the instrument. |
| `sweep` | `str` | The sweep (e.g., “Sweep 1”) the instrument belongs to. |
| `metadata` | `dict | None` | Optional key/value data (URL, DOI, copyright, etc.). |

The model is used to store and transfer catalogue instrument data, and it can be validated or serialized by Pydantic.

**Imports:**
```
from pydantic import BaseModel, Field
```
