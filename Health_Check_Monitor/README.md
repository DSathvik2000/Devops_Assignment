## **:floppy_disk: Backup Script**
📂 **File:** `Backup.py`  
📝 **Description:**  
This script automates **file backup** by copying files from a **source directory** to a **destination directory**. If a file already exists, it appends a **timestamp** to prevent overwriting.

### ✅ **Features**
✔️ **Ensures unique backups** without overwriting  
✔️ **Appends timestamps** for duplicate filenames  
✔️ **Handles missing directories gracefully**  

### 📌 **Usage**
```sh
python Backup.py /path/to/source /path/to/destination
```
⚠️ Prerequisites
- Ensure both source and destination directories exist.
- Requires Python 3.x installed, If Python is not installed, install it using:
  ```sh
  sudo apt update && sudo apt install python3 -y   # For Linux
  brew install python3                             # For macOS
  winget install Python.Python.3                   # For Windows (using Winget)
  ```
 - Clone the repository
    ```sh
    git clone https://github.com/yourusername/repository.git
    cd repository
    ```



   
