# draw_cosine_similarity_matrix (function)

**Code:**
```python
def draw_cosine_similarity_matrix(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
    """
        Draws a heatmap of the cosine similarity matrix based on the given questions.

        Args:
            questions: List of question strings to visualize
            ax: Matplotlib Axes object to draw on
            canvas: Tkinter canvas for displaying the plot
    """
    embedding_matrix = convert_texts_to_vector(questions)
    similarity_matrix = cosine_similarity(embedding_matrix)

    ax.clear()
    ax.axis("on")
    ax.tick_params(
        axis="both",
        which="both",
        bottom=True,
        left=True,
        labelbottom=True,
        labelleft=True
    )
    ax.set_title("Cosine Similarity Matrix")

    ax.imshow(similarity_matrix, cmap="Blues", interpolation="nearest")
    ax.invert_yaxis()
    canvas.draw()
```

**Explanation:**
**What it does**

`draw_cosine_similarity_matrix` takes a list of question strings and visualises how similar each pair of questions is.

1. **Vectorise the text** – `convert_texts_to_vector(questions)` turns every question into a numeric embedding (a row in `embedding_matrix`).
2. **Compute similarities** – `cosine_similarity(embedding_matrix)` returns a square matrix where each entry is the cosine similarity between two question vectors.
3. **Draw the heatmap**  
   * Clears the current Matplotlib `ax`.  
   * Turns the axis on and sets tick parameters.  
   * Gives the plot a title.  
   * Uses `ax.imshow` to show the similarity matrix as a blue‑to‑white heatmap.  
   * Inverts the y‑axis so the first question appears at the top.
4. **Refresh the Tkinter canvas** – `canvas.draw()` updates the GUI with the new plot.

**Parameters**

- `questions`: list of strings to compare.  
- `ax`: the Matplotlib Axes object where the heatmap will be drawn.  
- `canvas`: the Tkinter `FigureCanvasTkAgg` that displays the Matplotlib figure in the GUI.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
