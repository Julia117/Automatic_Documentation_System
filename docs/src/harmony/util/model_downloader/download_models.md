# download_models (function)

**Code:**
```python
def download_models(is_force=False):
    """
    Downloads spaCy models to local path HARMONY_SPACY_PATH, defaulting to home directory.
    """
    local_path = os.getenv("HARMONY_SPACY_PATH", os.path.expanduser("~") + "/harmony")

    print(
        "Downloading spaCy models to " + local_path + ".\nSet environment variable HARMONY_SPACY_PATH if you want to change model file location.")

    # Base URL of the model files in Azure Blob Storage static hosted site.
    url = "https://harmonyapistorage.z33.web.core.windows.net/harmony_spacy_models.tar.bz2"

    if os.path.exists(local_path + "/harmony_spacy_models"):
        if not is_force:
            print("Error: Path already exists on your computer: ", local_path + "/harmony_spacy_models")
            print("Exiting spaCy model downloader.\nRun download_models(True) to force redownload.")
            return
        else:
            print("Removing ", local_path + "/harmony_spacy_models")
            shutil.rmtree(local_path + "/harmony_spacy_models")
            print("Removed ", local_path + "/harmony_spacy_models")

    if not os.path.exists(local_path):
        os.makedirs(local_path)

    tmpfile = local_path + "/harmony_spacy_models.tar.bz2"

    print(f"Downloading {url} to {tmpfile}...")

    wget.download(url, out=tmpfile, bar=bar_custom)

    print(f"Downloaded {url} to {tmpfile}.")
    print(f"Unzipping {tmpfile}...")

    file = tarfile.open(tmpfile)
    file.extractall(local_path)

    print(f"\tWrote models to {local_path}")

    print(f"Deleting {tmpfile}...")
    os.remove(tmpfile)
    print(f"Deleted {tmpfile}.")
```

**Explanation:**
**`download_models(is_force=False)` – Quick‑start guide**

| What it does | How it works |
|--------------|--------------|
| **Downloads spaCy language models** from a fixed Azure URL and installs them locally. | 1. **Target folder** – Looks for the env var `HARMONY_SPACY_PATH`. If not set, defaults to `~/harmony`. |
| | 2. **Safety check** – If the folder `~/harmony/harmony_spacy_models` already exists: <br>• If `is_force` is `False`, it aborts and tells you to run `download_models(True)` to overwrite.<br>• If `is_force` is `True`, it deletes the existing folder before proceeding. |
| | 3. **Create base folder** – Makes the target directory if it doesn’t exist. |
| | 4. **Download** – Uses `wget.download` to fetch `harmony_spacy_models.tar.bz2` into a temporary file inside the target folder. |
| | 5. **Extract** – Opens the tarball with `tarfile` and extracts all contents into the target folder. |
| | 6. **Cleanup** – Deletes the downloaded tarball after extraction. |
| | 7. **Logging** – Prints progress messages at each step so you can see what’s happening. |

**Key points for developers**

* **Environment variable**: Set `HARMONY_SPACY_PATH` if you want the models stored elsewhere.
* **Force re‑download**: Call `download_models(True)` to replace any existing installation.
* **No return value** – The function simply writes files to disk; you can check the folder to confirm success.

**Imports:**
```
import os, import shutil, import sys, import tarfile, import wget
```
