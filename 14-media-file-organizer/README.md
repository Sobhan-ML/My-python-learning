# Interactive Media File Organizer 🗂️

A Python automation script that traverses a messy directory, identifies media files (photos and videos), and neatly sorts copies of them into a structured destination folder based on their modification year. 

## Logic & Workflow
1. **Interactive Prompt:** The program asks the user to input the source and destination paths dynamically during runtime. It validates the source path to prevent runtime crashes.
2. **File Scanning:** Uses `os.walk()` to recursively search through all files and subdirectories within the source.
3. **Categorization:** Uses `os.path.splitext()` to separate the filename from its extension, routing matching extensions to either a `photos` or `videos` category.
4. **Metadata Extraction:** Reads the system's modification time of each file using `os.path.getmtime()` to determine its creation/modification year.
5. **Binary Copying:** Safely replicates the files into their new chronological directories (`Year/Category/`) using Python's native binary read/write context managers (`rb` and `wb`).

## How to Run
Simply run the script in your IDE (like VSCode or PyCharm) or via terminal:
```bash
python main.py