# MatchResult (class)

**Code:**
```python
class MatchResult(BaseModel):
    """
    For use internally in the Python library but *not* the API because the NDarrays don't serialise.
    The API will put most of the fields from this object in a MatchResponse object which is serialisable.
    """
    questions: List[Question] = Field(
        description="The questions which were matched, in an order matching the order of the matrix"
    )
    similarity_with_polarity: Any = Field(description="Matrix of cosine similarity matches for the questions")
    response_options_similarity: Any = Field(description="Matrix of cosine similarity matches for the response options")
    query_similarity: Any = Field(
        None, description="Similarity metric between query string and items"
    )
    new_vectors_dict: dict = Field(
        None,
        description="Vectors for the cache. These should be stored by the Harmony API to reduce unnecessary calls to the LLM"
    )
    instrument_to_instrument_similarities: List[InstrumentToInstrumentSimilarity] = Field(
        None, description="A list of similarity values (precision, recall, F1) between instruments"
    )
    clusters: List[HarmonyCluster] = Field(description="The clusters in the set of questions")
```

**Explanation:**
**MatchResult – internal helper object**

`MatchResult` is a Pydantic model that the Harmony Python library builds after it finishes matching instruments and questions.  
It’s **not** meant to be sent over the network – the NumPy arrays inside it can’t be JSON‑serialised – so the API layer copies the data into a `MatchResponse` that is serialisable.

Key fields (in plain language)

| Field | What it holds |
|-------|---------------|
| `questions` | The list of `Question` objects that were processed, in the same order as the similarity matrix. |
| `similarity_with_polarity` | A 2‑D array (NumPy) of cosine similarities between every pair of questions, with a polarity (+/-) applied to indicate whether the match is “positive” or “negative”. |
| `response_options_similarity` | Similarity matrix for the response‑option strings of the questions. |
| `query_similarity` | Cosine similarity scores between the user’s query string and each question (if a query was supplied). |
| `new_vectors_dict` | A cache of text‑to‑vector mappings that the API can store to avoid re‑calling the LLM. |
| `instrument_to_instrument_similarities` | A list of `InstrumentToInstrumentSimilarity` objects, each giving precision, recall and F1 for a pair of instruments. |
| `clusters` | The clusters of questions produced by the chosen clustering algorithm (each cluster is a `HarmonyCluster`). |

In short: **MatchResult** bundles all the raw, NumPy‑heavy results of the matching process so the library can work with them internally, while the API layer translates them into a lightweight, serialisable `MatchResponse`.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
