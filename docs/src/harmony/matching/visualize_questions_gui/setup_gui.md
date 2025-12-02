# setup_gui (function)

**Code:**
```python
def setup_gui(questions: List[str]):
    """
        Sets up the Tkinter GUI.

        Args:
            questions: List of question strings to visualize.
    """

    def add_question(questions: List[str], ax: Axes, canvas: FigureCanvasTkAgg):
        """Handles adding new questions through a simple dialog and updates the canvas"""
        question = tkinter.simpledialog.askstring("Add a New Question", "New Question:")
        if question:
            questions.append(question)
            # redraw cosine similarity matrix including newly added question
            draw_cosine_similarity_matrix(questions, ax, canvas)

    def display_questions():
        """Displays all questions in a scrollable dialog window"""
        dialog = tk.Toplevel(root)
        dialog.title("All Questions")
        dialog.geometry("400x600")

        # make the dialog window modal
        dialog.grab_set()
        dialog.focus_set()
        root.attributes("-disabled", True)

        scrollbar = ttk.Scrollbar(dialog)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        questions_text = tk.Text(dialog, height=8)
        questions_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, )

        questions_text["yscrollcommand"] = scrollbar.set
        scrollbar.config(command=questions_text.yview)

        for i, question in enumerate(questions):
            questions_text.insert(tk.END, f"Q{i}: {question}\n")

        def close_dialog():
            """Cleanup when closing the dialog"""
            root.attributes("-disabled", False)
            dialog.destroy()

        dialog.protocol("WM_DELETE_WINDOW", close_dialog)

        dialog.transient(root)
        dialog.wait_window()

    # main window
    root = tk.Tk()
    root.title("Harmony Visualizer")
    root.geometry("800x450")

    # main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # left frame for graphs
    graph_frame = tk.Frame(main_frame, width=350, height=350, bg="white")
    graph_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    graph_frame.pack_propagate(False)

    # upper right frame for graph buttons
    button_frame = tk.Frame(main_frame, width=200, bg="lightgray")
    button_frame.pack(side=tk.RIGHT, fill=tk.Y)
    # lower right frame with buttons for displaying and adding questions
    bottom_button_frame = tk.Frame(button_frame, bg="lightgray")
    bottom_button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    fig, ax = plt.subplots()
    ax.axis("off")  # hide placeholder chart until a button is pressed
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # the graph buttons and their corresponding draw functions
    button_texts = ["Cosine Similarity Matrix", "Cluster Scatter Plot", "Network Graph"]
    button_functions = [draw_cosine_similarity_matrix, draw_clusters_scatter_plot, draw_network_graph]

    for button_text, function in zip(button_texts, button_functions):
        new_button = tk.Button(button_frame, text=button_text,
                               command=lambda func=function: func(questions, ax, canvas))
        new_button.pack(pady=8, padx=10, fill=tk.X)

    # buttons for adding and displaying questions
    add_question_button = tk.Button(bottom_button_frame, text="Add Question",
                                    command=lambda func=add_question: func(questions, ax, canvas))
    display_questions_button = tk.Button(bottom_button_frame, text="See Questions", command=display_questions)
    add_question_button.pack(pady=8, padx=10, fill=tk.X)
    display_questions_button.pack(pady=8, padx=10, fill=tk.X)

    root.protocol("WM_DELETE_WINDOW", lambda: (plt.close("all"), root.destroy()))
    root.mainloop()
```

**Explanation:**
**`setup_gui(questions)` – Quick developer‑level rundown**

| What it does | How it works |
|--------------|--------------|
| **Creates the main window** | `root = tk.Tk()` – a 800×450 window titled “Harmony Visualizer”. |
| **Layout** | 3 main areas:<br>• Left: `graph_frame` – where the Matplotlib plot lives.<br>• Right: `button_frame` – holds three graph‑type buttons.<br>• Bottom of the right side: `bottom_button_frame` – “Add Question” and “See Questions” buttons. |
| **Plot canvas** | `fig, ax = plt.subplots()` – hidden until a button is pressed. `FigureCanvasTkAgg` embeds the Matplotlib figure into `graph_frame`. |
| **Graph buttons** | For each of the three visualisations (`draw_cosine_similarity_matrix`, `draw_clusters_scatter_plot`, `draw_network_graph`) a button is created. Clicking it calls the function with the current `questions`, `ax`, and `canvas`. |
| **Add question** | `add_question` pops a simple dialog (`tkinter.simpledialog.askstring`). If the user enters text, it appends it to `questions` and immediately redraws the cosine‑similarity heatmap. |
| **Show all questions** | `display_questions` opens a modal `Toplevel` window with a scrollable `Text` widget listing every question. Closing the dialog re‑enables the main window. |
| **Cleanup** | On window close, all Matplotlib figures are closed and the Tkinter app exits. |

In short, `setup_gui` wires together a Tkinter window, a Matplotlib canvas, and a set of buttons that let users view different visualisations of the supplied question list and add new questions on the fly.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
