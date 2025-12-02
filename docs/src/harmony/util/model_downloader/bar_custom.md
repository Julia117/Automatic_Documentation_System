# bar_custom (function)

**Code:**
```python
def bar_custom(current, total, width=80):
    """
    Display a progress bar to track the download.
    :param current: Current bytes downloaded
    :param total: Total bytes.
    :param width: Width of the bar in chars.
    """
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total), end="\r")
```

**Explanation:**
**`bar_custom` – a tiny progress‑bar helper**

```python
def bar_custom(current, total, width=80):
    """
    Display a progress bar to track the download.
    :param current: Current bytes downloaded
    :param total: Total bytes.
    :param width: Width of the bar in chars.
    """
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total), end="\r")
```

- **Purpose**: Show a one‑line download progress in the console.
- **Parameters**  
  - `current`: bytes downloaded so far.  
  - `total`: total bytes to download.  
  - `width`: unused in this implementation (kept for API compatibility).
- **How it works**  
  1. Calculates the percentage (`current / total * 100`).  
  2. Prints a formatted string: `"Downloading: X% [current / total] bytes"`.  
  3. Uses `end="\r"` so the next call overwrites the same line, giving a live‑update effect.

It’s a minimal, non‑graphical progress indicator suitable for command‑line downloads.

**Imports:**
```
import os, import shutil, import sys, import tarfile, import wget
```
