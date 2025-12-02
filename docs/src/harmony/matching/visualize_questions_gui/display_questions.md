# display_questions (function)

**Code:**
```python
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
```

**Explanation:**
**`display_questions()` – quick rundown for developers**

```python
def display_questions():
    """Displays all questions in a scrollable dialog window"""
```

1. **Create a modal dialog**  
   - `tk.Toplevel(root)` opens a new window that blocks interaction with the main window (`root`).  
   - `grab_set()` and `focus_set()` make it modal; the main window is disabled with `root.attributes("-disabled", True)`.

2. **Layout**  
   - A vertical `ttk.Scrollbar` is packed on the right.  
   - A `tk.Text` widget (height 8 lines) is packed on the left, set to expand and fill the remaining space.  
   - The scrollbar is linked to the text widget (`yscrollcommand` and `command`).

3. **Populate the text widget**  
   - Iterate over the global `questions` list, inserting each as `Q{i}: <question>\n`.

4. **Close handling**  
   - `close_dialog()` re‑enables the main window and destroys the dialog.  
   - `dialog.protocol("WM_DELETE_WINDOW", close_dialog)` ensures this runs when the user clicks the close button.

5. **Finalize**  
   - `dialog.transient(root)` keeps the dialog on top of the main window.  
   - `dialog.wait_window()` pauses execution until the dialog is closed.

**Result:** A simple, scrollable pop‑up that lists all current questions, preventing interaction with the main GUI until the user closes it.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
