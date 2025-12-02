# add_question (function)

**Code:**
```python
def add_question(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
        """Handles adding new questions through a simple dialog and updates the canvas"""
        question = tkinter.simpledialog.askstring("Add a New Question", "New Question:")
        if question:
            questions.append(question)
            # redraw cosine similarity matrix including newly added question
            draw_cosine_similarity_matrix(questions, ax, canvas)
```

**Explanation:**
**`add_question` – quick recap**

```python
def add_question(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
    """Handles adding new questions through a simple dialog and updates the canvas"""
    question = tkinter.simpledialog.askstring("Add a New Question", "New Question:")
    if question:
        questions.append(question)
        # redraw cosine similarity matrix including newly added question
        draw_cosine_similarity_matrix(questions, ax, canvas)
```

- **Purpose**: Let the user type a new question, add it to the existing list, and immediately refresh the visual display.
- **Parameters**  
  - `questions`: the current list of question strings (modified in‑place).  
  - `ax`: the Matplotlib `Axes` object that holds the current plot.  
  - `canvas`: the `FigureCanvasTkAgg` that renders the plot in the Tkinter window.
- **Workflow**  
  1. Show a simple input dialog (`askstring`).  
  2. If the user enters text, append it to `questions`.  
  3. Call `draw_cosine_similarity_matrix` to recompute the similarity matrix and redraw the heatmap on the same `ax`/`canvas`.  

This keeps the GUI responsive: every new question instantly updates the similarity heatmap.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
