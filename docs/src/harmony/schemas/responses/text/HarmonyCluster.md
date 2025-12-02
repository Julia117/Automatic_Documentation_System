# HarmonyCluster (class)

**Code:**
```python
class HarmonyCluster(BaseModel):
    """
    Defines a cluster of questionnaire items
    """
    cluster_id: int = Field(
        description="The ID of this cluster")
    centroid_id: int = Field(description="The ID of the central question in this cluster")
    centroid: Question = Field(description="The central question", exclude=True, )
    item_ids: List[int] = Field(description="The IDs of questions within this cluster")
    items: List[Question] = Field(description="The questions within this cluster", exclude=True, )
    text_description: str = Field(description="Text describing the cluster")
    keywords: List[str] = Field(description="Cluster keywords/topics that best summarise the cluster")
```

**Explanation:**
**HarmonyCluster** is a lightweight data container that groups together questionnaire items that are similar to each other.

| Field | Purpose |
|-------|---------|
| `cluster_id` | Unique number identifying the cluster. |
| `centroid_id` | Index of the “central” question in the cluster (the one that best represents the group). |
| `centroid` | The actual `Question` object that is the cluster’s centroid. It’s excluded from JSON output to keep the payload small. |
| `item_ids` | List of indices of all questions that belong to this cluster. |
| `items` | The full `Question` objects in the cluster (also excluded from JSON). |
| `text_description` | A human‑readable description of the cluster, usually the centroid’s text. |
| `keywords` | Short list of words that capture the main topics of the cluster. |

In short, a `HarmonyCluster` holds the metadata and content of a group of related questions, making it easy to pass around, serialize, or display cluster information in the rest of the system.

**Imports:**
```
from typing import List, Any, from pydantic import BaseModel, Field, RootModel, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.requests.text import Instrument, from harmony.schemas.requests.text import Question
```
