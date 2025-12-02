# draw_network_graph (function)

**Code:**
```python
def draw_network_graph(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
    """
        Draws a network graph based on the given questions, where edges represent high similarity (>0.5).
        Communities are detected using greedy modularity optimization.

        Args:
            questions: List of question strings to visualize
            ax: Matplotlib Axes object to draw on
            canvas: Tkinter canvas for displaying the plot
    """
    embedding_matrix = convert_texts_to_vector(questions)
    similarity_matrix = cosine_similarity(embedding_matrix)

    ax.clear()
    ax.axis("off")
    ax.set_aspect("auto")
    ax.set_title("Network Cluster Graph")

    G = nx.Graph()
    n = similarity_matrix.shape[0]

    i = 0
    for i in range(n):
        for j in range(i + 1, n):
            if similarity_matrix[i, j] > 0.5:
                G.add_edge(i, j, weight=similarity_matrix[i, j])

    communities = list(community.greedy_modularity_communities(G))

    # assign colors to nodes based on communities
    node_color = []
    for comm_idx, comm in enumerate(communities):
        for _ in comm:
            node_color.append(comm_idx)

    # improve node positions using existing layouts
    pos = nx.kamada_kawai_layout(G, weight="weight")
    pos = nx.spring_layout(
        G,
        pos=pos,
        k=2,
        scale=2.0,
        iterations=200
    )

    nx.draw_networkx_nodes(
        G, pos,
        ax=ax,
        node_size=300,
        node_color=node_color,
    )

    nx.draw_networkx_edges(
        G, pos,
        ax=ax,
        width=1.0,
        alpha=0.7
    )

    nx.draw_networkx_labels(
        G, pos,
        ax=ax,
        font_size=12
    )

    canvas.draw()
```

**Explanation:**
**`draw_network_graph` – quick‑start guide**

| What it does | How it works | Why it matters |
|--------------|--------------|----------------|
| **Visualises question similarity as a network** | 1. **Embed** each question string into a vector (`convert_texts_to_vector`).  <br>2. Compute pairwise cosine similarity (`cosine_similarity`).  <br>3. Build an undirected graph `G` where an edge is added between two questions if their similarity > 0.5.  <br>4. Detect communities (clusters) with NetworkX’s greedy modularity algorithm.  <br>5. Assign a colour to each node based on its community.  <br>6. Compute node positions first with Kamada‑Kawai, then refine with a spring layout.  <br>7. Draw nodes, edges, and labels on the supplied Matplotlib `ax`.  <br>8. Refresh the Tkinter canvas (`canvas.draw()`). | Gives a quick, interpretable visual of which questions are “close” and how they group together. The community colouring helps spot clusters without extra code. |

**Key points for developers**

- **Input**: `questions` – list of raw strings.  
- **Output**: A plotted network on the given `ax`; the canvas is updated automatically.  
- **Threshold**: Only similarities above 0.5 become edges; adjust if you need a denser or sparser graph.  
- **Community detection**: Uses `networkx.algorithms.community.greedy_modularity_communities`.  
- **Layout**: Two‑step layout (Kamada‑Kawai → spring) gives a stable, readable arrangement.  
- **Re‑draw**: `ax.clear()` and `canvas.draw()` ensure the plot refreshes cleanly each time the function is called.  

Use this function whenever you want a quick, interactive network view of question similarity in your Tkinter GUI.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
