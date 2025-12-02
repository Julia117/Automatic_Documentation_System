# close_dialog (function)

**Code:**
```python
def close_dialog():
            """Cleanup when closing the dialog"""
            root.attributes("-disabled", False)
            dialog.destroy()
```

**Explanation:**
**`close_dialog()` – what it does**

```python
def close_dialog():
    """Cleanup when closing the dialog"""
    root.attributes("-disabled", False)   # re‑enable the main window
    dialog.destroy()                     # close the dialog window
```

- **Re‑enable the main window** – The main application window (`root`) was disabled while the dialog was open (`root.attributes("-disabled", True)`). This function turns that back on so the user can interact with the main window again.
- **Destroy the dialog** – It then calls `dialog.destroy()` to remove the dialog from the screen and free its resources.

In short, `close_dialog()` restores the main window’s usability and closes the modal dialog.

**Imports:**
```
import sys, from typing import List, import numpy as np, from sklearn.cluster import KMeans, AffinityPropagation, from sklearn.decomposition import PCA, from sklearn.metrics.pairwise import cosine_similarity, from harmony.matching.default_matcher import convert_texts_to_vector
```
