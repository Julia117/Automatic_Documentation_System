# get_instrument_similarity (function)

**Code:**
```python
def get_instrument_similarity(instruments, similarity_with_polarity):
    instrument_start_pos = []
    instrument_end_pos = []
    cur_start = 0
    for instr_idx in range(len(instruments)):
        instrument_start_pos.append(cur_start)
        instrument_end_pos.append(cur_start + len(instruments[instr_idx].questions))
        cur_start += len(instruments[instr_idx].questions)

    instrument_to_instrument_similarities = []

    for i in range(len(instruments)):
        instrument_1 = instruments[i]
        for j in range(i + 1, len(instruments)):
            instrument_2 = instruments[j]
            item_to_item_similarity_matrix = similarity_with_polarity[instrument_start_pos[i]:instrument_end_pos[i],
                                             instrument_start_pos[j]:instrument_end_pos[j]]

            precision, recall, f1 = get_precision_recall_f1(item_to_item_similarity_matrix)

            instrument_to_instrument_similarities.append(
                InstrumentToInstrumentSimilarity(instrument_1_idx=i, instrument_2_idx=j,
                                                 instrument_1_name=instrument_1.instrument_name,
                                                 instrument_2_name=instrument_2.instrument_name, precision=precision,
                                                 recall=recall, f1=f1)
            )

    return instrument_to_instrument_similarities
```

**Explanation:**
**What it does**

`get_instrument_similarity` turns a big question‑by‑question similarity matrix into a list of *instrument‑level* similarity scores.

**How it works**

1. **Find where each instrument’s questions live in the matrix**  
   * `instrument_start_pos[i]` – index of the first question of instrument *i*  
   * `instrument_end_pos[i]` – index after the last question of instrument *i*  

2. **Loop over every unordered pair of instruments**  
   * Slice the big matrix to get the sub‑matrix that compares every question of instrument *i* with every question of instrument *j* (`item_to_item_similarity_matrix`).

3. **Compute precision, recall and F1** for that sub‑matrix using `get_precision_recall_f1`.

4. **Store the result** in an `InstrumentToInstrumentSimilarity` object that records the two instrument indices, names, and the three scores.

5. **Return** the list of all such similarity objects.

In short, it aggregates the fine‑grained question‑level similarities into a concise, pairwise instrument similarity report.

**Imports:**
```
import operator, import numpy as np, from harmony.schemas.responses.text import InstrumentToInstrumentSimilarity
```
