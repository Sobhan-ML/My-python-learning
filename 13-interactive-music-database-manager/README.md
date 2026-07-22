# Interactive Music Database Manager 🎵

An interactive, in-memory relational database tool that manages users, music albums, and performs real-time relational analytics through a terminal interface.

## Features
- **Dynamic Data Entry:** Allows users to interactively register new albums and users with metadata (demographics, track counts, genres).
- **Relational Analytics:** Performs dynamic filtering across multiple criteria (User/Artist, Age/Genre, City/Artist, etc.).
- **Pythonic Generator Expressions:** Uses optimized `sum()` and generator expressions instead of nested loops for fast queries.
- **Robust CLI Interface:** Protects execution with continuous `while/try/except` loops to gracefully handle invalid data inputs.

## How to Run
Execute the script in your terminal and interact with the menu:
```bash
python main.py