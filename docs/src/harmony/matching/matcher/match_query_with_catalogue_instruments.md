# match_query_with_catalogue_instruments (function)

**Code:**
```python
def match_query_with_catalogue_instruments(
        query: str,
        catalogue_data: dict,
        vectorisation_function: Callable,
        texts_cached_vectors: dict[str, List[float]],
        max_results: int = 100,
        is_negate: bool = True
) -> dict[str, Union[list, dict]]:
    """
    Match query with catalogue instruments.

    :param query: The query.
    :param catalogue_data: The catalogue data.
    :param vectorisation_function: A function to vectorize a text.
    :param texts_cached_vectors: A dictionary of already cached text vectors (text to vector).
    :param max_results: The max amount of instruments to return.
    :return: A dict containing the list of instruments (up to 100) and the new text vectors.
        E.g. {"instruments": [...], "new_text_vectors": {...}}.
    """

    response = {"instruments": [], "new_text_vectors": {}}

    # Catalogue data
    catalogue_instrument_idx_to_catalogue_questions_idx: List[List[int]] = (
        catalogue_data["instrument_idx_to_question_idx"]
    )
    all_catalogue_questions_embeddings_concatenated: np.ndarray = catalogue_data[
        "all_embeddings_concatenated"
    ]
    all_catalogue_instruments: List[dict] = catalogue_data["all_instruments"]

    # No embeddings = nothing to find
    if len(all_catalogue_questions_embeddings_concatenated) == 0:
        return response

    # Text vectors
    text_vectors, new_text_vectors = create_full_text_vectors(
        all_questions=[],
        query=query,
        vectorisation_function=vectorisation_function,
        texts_cached_vectors=texts_cached_vectors,
        is_negate=is_negate
    )

    # Get an array of dimensions
    vectors = np.array([text_vectors[0].vector])

    # Get a 2D array of 1 x (number of questions in catalogue)
    catalogue_similarities = cosine_similarity(
        vectors, all_catalogue_questions_embeddings_concatenated
    )

    # Get the catalogue questions similarities for the query
    catalogue_questions_similarities_for_query = catalogue_similarities[0].tolist()

    # Get indexes of top matching questions in the catalogue
    # The first index contains the best match
    top_catalogue_questions_matches_idxs = [
        catalogue_questions_similarities_for_query.index(i)
        for i in heapq.nlargest(max_results, catalogue_questions_similarities_for_query)
    ]

    # A dict of matching instruments
    # The key is the name of the instrument and the value is the instrument
    instrument_matches: OrderedDict[str, Instrument] = OrderedDict()

    # Find the matching instruments by looking for the instrument of the top catalogue questions matches indexes
    # Loop through indexes of top matched catalogue question
    for top_catalogue_question_match_idx in top_catalogue_questions_matches_idxs:
        # Loop through instrument index with its question indexes
        for catalogue_instrument_idx, catalogue_instrument_questions_idxs in enumerate(
                catalogue_instrument_idx_to_catalogue_questions_idx
        ):
            # Check if the index of the top matched catalogue question is in the catalogue instrument's question indexes
            if top_catalogue_question_match_idx in catalogue_instrument_questions_idxs:
                catalogue_instrument = all_catalogue_instruments[
                    catalogue_instrument_idx
                ]

                # Add the instrument to the dict if it wasn't already added
                instrument_name = catalogue_instrument["instrument_name"]
                if instrument_name not in instrument_matches:
                    instrument_matches[instrument_name] = Instrument.model_validate(
                        catalogue_instrument
                    )

    response["instruments"] = [x for x in instrument_matches.values()]
    response["new_text_vectors"] = new_text_vectors

    return response
```

**Explanation:**
**What it does**

`match_query_with_catalogue_instruments` takes a free‑text query and looks for the most relevant instruments in a pre‑built catalogue.

1. **Prepare the query vector**  
   * It calls `create_full_text_vectors` to turn the query string into a vector (using the supplied `vectorisation_function`).  
   * Any vectors that were already cached in `texts_cached_vectors` are reused; new ones are returned in `new_text_vectors`.

2. **Compute similarities**  
   * The query vector is compared against every question vector that exists in the catalogue (`all_embeddings_concatenated`) using cosine similarity.  
   * The result is a list of similarity scores, one per catalogue question.

3. **Pick the best matches**  
   * The function keeps the indices of the top `max_results` (default 100) most similar catalogue questions.

4. **Map questions back to instruments**  
   * For each of those top question indices it looks up which instrument(s) contain that question (`instrument_idx_to_question_idx`).  
   * It collects each unique instrument (by name) into an ordered dictionary, converting the raw catalogue dict into an `Instrument` Pydantic model.

5. **Return**  
   * `response["instruments"]` – a list of the matched `Instrument` objects (max 100).  
   * `response["new_text_vectors"]` – any new vectors that were generated for the query, so the caller can cache them.

**Why it’s useful**

* Quickly find the instruments that are most relevant to a user’s query.  
* Reuses cached embeddings to avoid repeated LLM calls.  
* Keeps the result deterministic (ordered by similarity) and limited to a sensible number of instruments.

**Imports:**
```
import heapq, import os, import pathlib, import statistics, from collections import Counter, OrderedDict, from typing import List, Callable, Optional, Union, import numpy as np, from numpy import dot, matmul, ndarray, matrix, from numpy.linalg import norm, from harmony.matching.deterministic_clustering import find_clusters_deterministic, from harmony.matching.affinity_propagation_clustering import cluster_questions_affinity_propagation, from harmony.matching.hdbscan_clustering import cluster_questions_hdbscan_from_embeddings, from harmony.matching.instrument_to_instrument_similarity import get_instrument_similarity, from harmony.matching.negator import negate, from harmony.schemas.catalogue_instrument import CatalogueInstrument, from harmony.schemas.catalogue_question import CatalogueQuestion, from harmony.schemas.requests.text import (
    Instrument,
    Question,
), from harmony.schemas.responses.text import MatchResult, from harmony.schemas.text_vector import TextVector, from harmony.matching.kmeans_clustering import cluster_questions_kmeans_from_embeddings, from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm, from langdetect import detect, DetectorFactory
```
