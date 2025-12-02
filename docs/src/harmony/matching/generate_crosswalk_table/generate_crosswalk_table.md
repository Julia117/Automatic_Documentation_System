# generate_crosswalk_table (function)

**Code:**
```python
def generate_crosswalk_table(instruments: List[Instrument], item_to_item_similarity_matrix: np.ndarray,
                             threshold: float = None, is_allow_within_instrument_matches=False,
                             is_enforce_one_to_one: bool = False) -> pd.DataFrame:
    """
    Generate a crosswalk table for a list of instruments, given the similarity matrix that came out of the match function. A crosswalk is a list of pairs of variables from different studies that can be harmonised.
    @param instruments: The original list of instruments, each containing a question. The sum of the number of questions in all instruments is the total number of questions which should equal both the width and height of the similarity matrix.
    @param item_to_item_similarity_matrix: The cosine similarity matrix from Harmony
    @param threshold: The minimum threshold that we consider a match. This is applied to the absolute match value. So if a question pair has similarity 0.2 and threshold = 0.5, then that question pair will be excluded. Leave as None if you don't want to apply any thresholding.
    @param is_allow_within_instrument_matches: Defaults to False. If this is set to True, we include crosswalk items that originate from the same instrument, which would otherwise be excluded by default.
    @param is_enforce_one_to_one: Defaults to False.  If this is set to True, we force all variables in the crosswalk table to be matched with exactly one other variable.
    @return: A crosswalk table as a DataFrame.
    """

    # assert that the similarity matrix is square
    assert item_to_item_similarity_matrix.shape[0] == item_to_item_similarity_matrix.shape[1]

    # assert that the similarity matrix is symmetric
    assert np.allclose(item_to_item_similarity_matrix, item_to_item_similarity_matrix.T)

    # assert that the similarity matrix is -1 <= x <= 1
    assert np.all(np.round(item_to_item_similarity_matrix, 3) >= -1.)
    assert np.all(np.round(item_to_item_similarity_matrix, 3) <= 1.)

    # assert that the similarity matrix has 1s on its diagonals
    assert np.allclose(np.diag(item_to_item_similarity_matrix), 1.)

    # ensure that the entries of the similarity matrix are floats
    if item_to_item_similarity_matrix.dtype != np.float64:
        item_to_item_similarity_matrix = item_to_item_similarity_matrix.astype(np.float64)


    matching_pairs = []

    all_questions = []
    for instrument_idx, instrument in enumerate(instruments):
        for question in instrument.questions:
            all_questions.append((instrument_idx, question))

    abs_similarities_between_instruments = np.abs(item_to_item_similarity_matrix)

    coord_to_sim = {}
    for question_2_idx in range(abs_similarities_between_instruments.shape[0]):
        for question_1_idx in range(abs_similarities_between_instruments.shape[1]):
            if question_2_idx > question_1_idx:
                coord_to_sim[(question_2_idx, question_1_idx)] = abs_similarities_between_instruments[
                    question_2_idx, question_1_idx]

    is_used_x = set()
    is_used_y = set()
    for (question_2_idx, question_1_idx), sim in sorted(coord_to_sim.items(), key=operator.itemgetter(1), reverse=True):
        if question_1_idx not in is_used_x and question_2_idx not in is_used_y and (
                threshold is None or abs_similarities_between_instruments[
            (question_2_idx, question_1_idx)] >= threshold):

            instrument_1_idx, question_1 = all_questions[question_1_idx]
            instrument_2_idx, question_2 = all_questions[question_2_idx]

            instrument_1 = instruments[instrument_1_idx]
            instrument_2 = instruments[instrument_2_idx]

            if not is_allow_within_instrument_matches and instrument_1_idx == instrument_2_idx:
                continue

            question_1_identifier = f"{instrument_1.instrument_name}_{question_1.question_no}"
            question_2_identifier = f"{instrument_2.instrument_name}_{question_2.question_no}"

            matching_pairs.append({
                'pair_name': f"{question_1_identifier}_{question_2_identifier}",
                'question1_id': question_1_identifier,
                'question1_text': question_1.question_text,
                'question2_id': question_2_identifier,
                'question2_text': question_2.question_text,
                'match_score': item_to_item_similarity_matrix[question_1_idx, question_2_idx]
            })

            # best_matches.add((question_1_idx,question_2_idx))
            if is_enforce_one_to_one:
                is_used_x.add(question_1_idx)
                is_used_y.add(question_2_idx)

    # convert list to dataframe
    return pd.DataFrame(matching_pairs)
```

**Explanation:**
**What it does**

`generate_crosswalk_table` turns a similarity matrix (cosine similarity between every pair of questions from a set of instruments) into a tidy table of the best matches.  
Each row in the returned `DataFrame` represents a pair of questions that can be “harmonised” – i.e., treated as the same concept in different studies.

**Parameters**

| Name | Meaning |
|------|---------|
| `instruments` | List of `Instrument` objects. Each instrument contains a list of `Question` objects. |
| `item_to_item_similarity_matrix` | Square NumPy array of cosine similarities. Rows/cols correspond to all questions in all instruments. |
| `threshold` | Minimum absolute similarity required for a pair to be kept. `None` means no filtering. |
| `is_allow_within_instrument_matches` | If `False` (default) pairs that come from the same instrument are dropped. |
| `is_enforce_one_to_one` | If `True`, once a question is matched it can’t be matched again (one‑to‑one mapping). |

**How it works**

1. **Sanity checks** – the matrix must be square, symmetric, values in `[-1,1]`, and 1 on the diagonal.  
2. **Flatten questions** – build a list `all_questions` that maps each matrix index to its instrument and question.  
3. **Collect upper‑triangle similarities** – create a dictionary `coord_to_sim` that holds the absolute similarity for each unique pair `(i,j)` where `j>i`.  
4. **Greedy matching** – iterate over the pairs sorted by similarity (highest first).  
   * Skip if either question is already used (unless `is_enforce_one_to_one` is `False`).  
   * Skip if the similarity is below `threshold`.  
   * Skip if the two questions belong to the same instrument and `is_allow_within_instrument_matches` is `False`.  
   * Otherwise record the pair: build identifiers (`instrumentName_questionNo`), store texts, and the raw similarity score.  
   * If `is_enforce_one_to_one` is `True`, mark both questions as used so they can’t be matched again.  
5. **Return** – convert the list of matched pairs into a `pandas.DataFrame`.

**Result**

The DataFrame has columns:

- `pair_name` – concatenated identifiers of the two questions.  
- `question1_id`, `question1_text` – info for the first question.  
- `question2_id`, `question2_text` – info for the second question.  
- `match_score` – the original similarity value (not absolute).

This table can be exported, visualised, or fed into downstream harmonisation pipelines.

**Imports:**
```
import operator, from typing import List, import numpy as np, import pandas as pd, from harmony.schemas.requests.text import Instrument
```
