# Question (class)

**Code:**
```python
class Question(BaseModel):
    question_no: Optional[str] = Field(None, description="Number of the question")
    question_intro: Optional[str] = Field(None, description="Introductory text applying to the question")
    question_text: str = Field(description="Text of the question")
    options: List[str] = Field([], description="The possible answer options")
    source_page: int = Field(0, description="The page of the PDF on which the question was located, zero-indexed")
    instrument_id: Optional[str] = Field(None, description="Unique identifier for the instrument (UUID-4)")
    instrument_name: Optional[str] = Field(None, description="Human readable name for the instrument")
    topics: Optional[list] = Field([], description="List of user-given topics with which to tag the questions")
    topics_auto: Optional[list] = Field(None, description="Automated list of topics identified by model")
    topics_strengths: Optional[dict] = Field(None,
                                             description="Automated list of topics identified by model with strength of topic")
    nearest_match_from_mhc_auto: Optional[dict] = Field(None, description="Automatically identified nearest MHC match")
    closest_catalogue_question_match: Optional[CatalogueQuestion] = Field(
        None, description="The closest question match in the catalogue for the question"
    )
    seen_in_catalogue_instruments: list[CatalogueInstrument] = Field(
        default=None, description="The instruments from the catalogue were the question was seen in"
    )
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "question_no": "1",
                "question_intro": "Over the last two weeks, how often have you been bothered by the following problems?",
                "question_text": "Feeling nervous, anxious, or on edge",
                "options": ["Not at all", "Several days", "More than half the days", "Nearly every day"],
                "source_page": 0
            }
        })
```

**Explanation:**
**`Question` – a Pydantic model that represents a single questionnaire item**

| Field | Type | Purpose |
|-------|------|---------|
| `question_no` | `Optional[str]` | The question’s number (e.g., “1”, “2.3”). Can be omitted. |
| `question_intro` | `Optional[str]` | Text that applies to the whole question block (e.g., “Over the last two weeks…”). |
| `question_text` | `str` | The actual question wording. Required. |
| `options` | `List[str]` | List of answer choices. Empty list if the question is open‑ended. |
| `source_page` | `int` | Zero‑based PDF page where the question was found. |
| `instrument_id` | `Optional[str]` | UUID of the instrument that owns this question. Filled automatically in `Instrument.model_post_init`. |
| `instrument_name` | `Optional[str]` | Human‑readable name of the instrument. |
| `topics` | `Optional[list]` | User‑supplied tags (e.g., `["anxiety", "sleep"]`). |
| `topics_auto` | `Optional[list]` | Tags inferred by the model. |
| `topics_strengths` | `Optional[dict]` | Model‑generated confidence scores for each auto‑tag. |
| `nearest_match_from_mhc_auto` | `Optional[dict]` | Auto‑identified nearest match from the MHC database. |
| `closest_catalogue_question_match` | `Optional[CatalogueQuestion]` | The best matching question from the catalogue. |
| `seen_in_catalogue_instruments` | `list[CatalogueInstrument]` | Instruments in the catalogue that contain this question. |

**Key points for developers**

1. **Validation & Serialization** – Inherits from `BaseModel`, so Pydantic handles type checking, defaults, and JSON conversion automatically.
2. **Optional vs Required** – Only `question_text` is mandatory; everything else can be omitted or left empty.
3. **Automatic ID propagation** – When an `Instrument` is created, its `instrument_id` is copied into each `Question` via `model_post_init`.
4. **Extensibility** – The model can be extended with more fields (e.g., `metadata`) without breaking existing code, thanks to Pydantic’s flexible schema handling.
5. **Example** – The `json_schema_extra` block shows a realistic instance, useful for documentation or auto‑generated API docs.

**Imports:**
```
import uuid, from typing import List, Optional, from pydantic import ConfigDict, BaseModel, Field, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.enums.file_types import FileType, from harmony.schemas.enums.languages import Language, from pydantic import ConfigDict, BaseModel, Field, from typing import Any, Dict, List, Optional
```
