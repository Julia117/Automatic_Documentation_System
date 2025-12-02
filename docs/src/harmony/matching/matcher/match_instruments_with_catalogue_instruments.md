# match_instruments_with_catalogue_instruments (function)

**Code:**
```python
def match_instruments_with_catalogue_instruments(
        instruments: List[Instrument],
        catalogue_data: dict,
        vectorisation_function: Callable,
        texts_cached_vectors: dict[str, List[float]],
        is_negate: bool = True
) -> tuple[List[Instrument], List[CatalogueInstrument]]:
    """
    Match instruments with catalogue instruments.

    :param instruments: The instruments.
    :param catalogue_data: The catalogue data.
    :param vectorisation_function: A function to vectorize a text.
    :param texts_cached_vectors: A dictionary of already cached vectors from texts (key is the text and value is the vector).
    :return: Index 0 in the tuple contains the list of instruments that now each contain the best instrument matches from the catalog.
        Index 1 in the tuple contains a list of closest instrument matches from the catalog for all the instruments.
    """

    # Gather all questions
    all_questions: List[str] = []
    for instrument in instruments:
        all_questions.extend([q.question_text for q in instrument.questions])
    all_questions = list(set(all_questions))

    # Create text vectors for all questions in all the uploaded instruments
    all_instruments_text_vectors, _ = create_full_text_vectors(
        all_questions=all_questions,
        query=None,
        vectorisation_function=vectorisation_function,
        texts_cached_vectors=texts_cached_vectors,
        is_negate=is_negate
    )

    # For each instrument, find the best instrument matches for it in the catalogue
    for instrument in instruments:
        instrument.closest_catalogue_instrument_matches = (
            match_questions_with_catalogue_instruments(
                questions=instrument.questions,
                catalogue_data=catalogue_data,
                all_instruments_text_vectors=all_instruments_text_vectors,
                questions_are_from_one_instrument=True,
            )
        )

    # Gather all questions from all instruments and find the best instrument matches in the catalogue
    all_instrument_questions: List[Question] = []
    for instrument in instruments:
        all_instrument_questions.extend(instrument.questions)
    closest_catalogue_instrument_matches = match_questions_with_catalogue_instruments(
        questions=all_instrument_questions,
        catalogue_data=catalogue_data,
        all_instruments_text_vectors=all_instruments_text_vectors,
        questions_are_from_one_instrument=False,
    )

    return instruments, closest_catalogue_instrument_matches
```

**Explanation:**
**`match_instruments_with_catalogue_instruments` – quick‑start guide**

| What it does | How it works | Why it matters |
|--------------|--------------|----------------|
| **Purpose** | For a list of user‑supplied instruments, find the most similar instruments that already exist in a pre‑built catalogue. | Lets you see which existing questionnaires are closest to the ones you just uploaded. |
| **Inputs** | - `instruments`: list of `Instrument` objects (each has a list of `Question`s).  <br> - `catalogue_data`: a dict that contains the catalogue’s questions, embeddings, and instrument metadata.  <br> - `vectorisation_function`: a callable that turns a string into a vector (e.g., a language‑model embedding).  <br> - `texts_cached_vectors`: a cache of already‑computed vectors to avoid re‑computing.  <br> - `is_negate`: whether to also vectorise the negated form of each question. | |
| **What it returns** | A tuple: <br> 1. The original `instruments` list, but each instrument now has a `closest_catalogue_instrument_matches` attribute containing the best‑matching catalogue instruments for that single instrument. <br> 2. A list of `CatalogueInstrument` objects that represent the best matches for **all** questions across all instruments combined. | Gives you both per‑instrument and overall catalogue matches. |

### Step‑by‑step

1. **Collect all unique questions**  
   ```python
   all_questions = list(set(q.question_text for i in instruments for q in i.questions))
   ```
   We only need each distinct question once for vectorisation.

2. **Vectorise every question**  
   ```python
   all_instruments_text_vectors, _ = create_full_text_vectors(
       all_questions=all_questions,
       query=None,
       vectorisation_function=vectorisation_function,
       texts_cached_vectors=texts_cached_vectors,
       is_negate=is_negate
   )
   ```
   `create_full_text_vectors` returns a list of `TextVector` objects (text + vector + flags).  
   It also uses the cache to skip already‑computed vectors.

3. **Find best catalogue match for each instrument**  
   For every instrument, call `match_questions_with_catalogue_instruments` with its own questions.  
   The helper returns a list of `CatalogueInstrument` objects (name, URL, source, etc.) that are the top matches for that instrument.  
   Store that list on the instrument (`instrument.closest_catalogue_instrument_matches`).

4. **Find best catalogue match for all questions together**  
   Combine all questions from all instruments into one list and run the same helper again, but with `questions_are_from_one_instrument=False`.  
   This gives a global ranking of catalogue instruments that best cover the entire set of questions.

5. **Return**  
   ```python
   return instruments, closest_catalogue_instrument_matches
   ```

### Why this helper exists

* **Performance** – vectorising each question only once (step 2) and re‑using those vectors for every instrument.  
* **Granularity** – you get per‑instrument matches (step 3) and an overall match (step 4).  
* **Reusability** – the heavy lifting of matching is delegated to `match_questions_with_catalogue_instruments`, keeping this function focused on orchestration.

That’s it: the function orchestrates vectorisation, per‑instrument matching, and global matching, returning enriched instruments and a list of the best catalogue instruments.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
