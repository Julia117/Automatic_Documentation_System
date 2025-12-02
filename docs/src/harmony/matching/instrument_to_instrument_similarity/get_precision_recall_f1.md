# get_precision_recall_f1 (function)

**Code:**
```python
def get_precision_recall_f1(item_to_item_similarity_matrix: np.ndarray) -> tuple:
    abs_similarities_between_instruments = np.abs(item_to_item_similarity_matrix)

    coord_to_sim = {}
    for y in range(abs_similarities_between_instruments.shape[0]):
        for x in range(abs_similarities_between_instruments.shape[1]):
            coord_to_sim[(y, x)] = abs_similarities_between_instruments[y, x]

    best_matches = set()
    is_used_x = set()
    is_used_y = set()
    for (y, x), sim in sorted(coord_to_sim.items(), key=operator.itemgetter(1), reverse=True):
        if x not in is_used_x and y not in is_used_y and abs_similarities_between_instruments[(y, x)] >= 0:
            best_matches.add((x, y))

            is_used_x.add(x)
            is_used_y.add(y)

    precision = len(is_used_x) / abs_similarities_between_instruments.shape[1]
    recall = len(is_used_y) / abs_similarities_between_instruments.shape[0]

    f1 = np.mean((precision, recall))

    return precision, recall, f1
```

**Explanation:**
**What the function does (in plain language)**  

`get_precision_recall_f1` takes a square matrix of cosine similarities between every question in one instrument and every question in another instrument.  
It treats each cell as a potential “match” between a question from instrument A (column x) and a question from instrument B (row y).  

1. **Absolute values** – It first takes the absolute value of every similarity so that negative scores are treated the same as positive ones.  
2. **Greedy one‑to‑one matching** –  
   * It builds a list of all (row, column) pairs sorted from highest similarity to lowest.  
   * It walks this list and picks a pair only if neither the row nor the column has already been matched.  
   * The chosen pairs are stored in `best_matches`.  
3. **Precision & recall** –  
   * **Precision** = how many columns (questions from instrument A) were matched, divided by the total number of columns.  
   * **Recall** = how many rows (questions from instrument B) were matched, divided by the total number of rows.  
4. **F1** – The function simply averages the precision and recall (`np.mean((precision, recall))`).  
5. **Return** – It returns a tuple `(precision, recall, f1)`.

In short, the function finds the best one‑to‑one mapping between two sets of questions, then reports how many questions from each side were successfully matched (precision/recall) and a combined score (F1).

**Imports:**
```
import operator, import numpy as np, from harmony.schemas.responses.text import InstrumentToInstrumentSimilarity
```
