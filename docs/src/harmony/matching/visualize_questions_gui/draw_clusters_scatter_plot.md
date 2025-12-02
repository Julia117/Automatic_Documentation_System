# draw_clusters_scatter_plot (function)

**Code:**
```python
def draw_clusters_scatter_plot(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
    """
        Draws a scatter plot based on the given questions.
        Uses K-Means clustering for small datasets (<30 questions) and Affinity Propagation clustering for larger ones.

        Args:
            questions: List of question strings to visualize
            ax: Matplotlib Axes object to draw on
            canvas: Tkinter canvas for displaying the plot
    """
    embedding_matrix = convert_texts_to_vector(questions)

    if len(questions) < 30:
        clustering = KMeans(n_clusters=5)
        labels = clustering.fit_predict(embedding_matrix)

        title = "K-Means Clustering"
    else:
        item_to_item_similarity_matrix = np.array(cosine_similarity(embedding_matrix)).astype(np.float64)

        clustering = AffinityPropagation(affinity="precomputed", damping=0.7, random_state=1, max_iter=200,
                                         convergence_iter=15)
        clustering.fit(np.abs(item_to_item_similarity_matrix))
        labels = clustering.labels_

        title = "Affinity Propagation Clustering"

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
    ax.set_aspect("auto")
    ax.set_title(title)

    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embedding_matrix)

    ax.scatter(
        reduced_embeddings[:, 0],
        reduced_embeddings[:, 1],
        c=labels,
        cmap="viridis",
        s=100
    )

    for i, point in enumerate(reduced_embeddings):
        ax.annotate(
            str(i),
            xy=(point[0], point[1]),
            xytext=(8, -10),
            textcoords="offset points",
            fontsize=8,
            color="black",
            ha="center"
        )

    canvas.draw()
```

**Explanation:**
**`draw_clusters_scatter_plot` – quick visualisation helper**

*Purpose*  
Takes a list of question strings, turns them into vectors, clusters the vectors, reduces the dimensionality to 2‑D, and draws a coloured scatter plot in a Matplotlib `Axes` that is shown on a Tkinter canvas.

*How it works*

1. **Vectorise**  
   `convert_texts_to_vector(questions)` → `embedding_matrix` (each row = question embedding).

2. **Choose clustering algorithm**  
   * If fewer than 30 questions → `KMeans(n_clusters=5)`  
   * Otherwise → `AffinityPropagation` on the cosine‑similarity matrix (pre‑computed, absolute values).  
   The resulting cluster labels are stored in `labels`.

3. **Prepare the plot**  
   * Clear the axes, enable ticks, set title to the algorithm used.
   * Run `PCA(n_components=2)` on the embeddings → `reduced_embeddings` (2‑D coordinates).

4. **Draw points**  
   * `ax.scatter` plots each point coloured by its cluster label (`c=labels`).
   * Annotate each point with its index (`0, 1, …`) for easy reference.

5. **Render**  
   `canvas.draw()` updates the Tkinter canvas with the new figure.

*Result*  
A quick, interactive scatter plot that shows how the questions group together, automatically switching between K‑Means for small sets and Affinity Propagation for larger ones.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
