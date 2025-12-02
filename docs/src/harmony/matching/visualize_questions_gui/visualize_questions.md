# visualize_questions (function)

**Code:**
```python
def visualize_questions(questions: List[str]):
    """
        Entry point for the GUI.

        Args:
            questions: List of question strings to visualize
    """
    if not questions:
        print("No questions provided. Exiting...")
        sys.exit(1)
    setup_gui(questions)
```

**Explanation:**
**`visualize_questions` – what it does**

```python
def visualize_questions(questions: List[str]):
    """
    Entry point for the GUI.

    Args:
        questions: List of question strings to visualize
    """
    if not questions:
        print("No questions provided. Exiting...")
        sys.exit(1)
    setup_gui(questions)
```

1. **Purpose**  
   *This is the public function you call to launch the whole visualisation tool.*  
   It takes a list of question strings and opens a Tkinter window that lets the user see and interact with those questions.

2. **Behaviour**  
   * **Empty list check** – If the caller passes an empty list, the function prints a short message and stops the program (`sys.exit(1)`).  
   * **Start GUI** – If there are questions, it hands the list over to `setup_gui`, which builds the window, buttons, plots, etc.

3. **Why it’s simple**  
   * All heavy lifting (creating frames, drawing plots, handling button clicks) lives in `setup_gui`.  
   * `visualize_questions` is just a guard‑rail and a dispatcher, making it easy to test or replace the GUI later.

**Bottom line for developers**  
Call `visualize_questions(my_questions)` with a non‑empty list of strings. If the list is empty, the program will exit with an error message. Otherwise, a Tkinter window will appear, letting users view and manipulate the questions.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
