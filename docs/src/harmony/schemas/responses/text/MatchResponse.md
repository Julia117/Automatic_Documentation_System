# MatchResponse (class)

**Code:**
```python
class MatchResponse(BaseModel):
    """
    This is serialisable (no Numpy objects inside) and can be returned by FastAPI.
    It's the API counterpart to MatchResult, which is the response object returned by the Python library.
    """
    instruments: List[Instrument] = Field(description="A list of instruments")
    questions: List[Question] = Field(
        description="The questions which were matched, in an order matching the order of the matrix"
    )
    matches: List[List] = Field(description="Matrix of cosine similarity matches for the questions")
    query_similarity: List = Field(
        None, description="Similarity metric between query string and items"
    )
    closest_catalogue_instrument_matches: List[CatalogueInstrument] = Field(
        default=[],
        description="The closest catalogue instrument matches in the catalogue for all the instruments, "
                    "the first index contains the best match etc."
    )
    instrument_to_instrument_similarities: List[InstrumentToInstrumentSimilarity] = Field(
        None, description="A list of similarity values (precision, recall, F1) between instruments"
    )
    clusters: List[HarmonyCluster] = Field(description="The clusters in the set of questions")
    response_options_similarity: List[List] = Field(description="Matrix of cosine similarity matches for the response options")
```

**Explanation:**
**MatchResponse – the API‑ready result**

`MatchResponse` is a Pydantic `BaseModel` that FastAPI can return as JSON.  
It is the “public” version of the internal `MatchResult` object – all the heavy NumPy arrays are replaced with plain Python lists so the data can be serialised.

| Field | What it holds | Why it matters |
|-------|---------------|----------------|
| `instruments` | List of `Instrument` objects that were processed | Gives the caller the original instruments that were harmonised |
| `questions` | List of `Question` objects (in the same order as the similarity matrix) | Lets the caller see each question that was matched |
| `matches` | 2‑D list of cosine‑similarity scores between each question and every other question | The core similarity matrix used for clustering, ranking, etc. |
| `query_similarity` | Optional list of similarity scores between the user’s query string and each question | Useful when a search term was supplied |
| `closest_catalogue_instrument_matches` | List of `CatalogueInstrument` objects (sorted by best match first) | Shows the top catalogue instruments that best match the user’s instruments |
| `instrument_to_instrument_similarities` | Optional list of `InstrumentToInstrumentSimilarity` objects | Precision/recall/F1 scores for every pair of instruments |
| `clusters` | List of `HarmonyCluster` objects | The clusters that were found among the questions |
| `response_options_similarity` | 2‑D list of cosine‑similarity scores between the concatenated response options of each question | Helps evaluate how similar the answer choices are across questions |

In short, `MatchResponse` packages all the results of a harmonisation run into a JSON‑friendly structure that FastAPI can send back to a client.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
