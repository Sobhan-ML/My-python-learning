# Minesweeper Board Generator 💣

A Python utility that generates a classic Minesweeper grid. It takes grid dimensions and mine coordinates, then automatically calculates the numeric values for all non-mine cells based on their proximity to the mines.

## Logic & Workflow
1. **Grid Initialization:** Creates an `N x M` matrix filled with `0`s.
2. **Mine Placement:** Places `*` at the specific coordinates provided by the user (converting 1-indexed human input to 0-indexed Python lists).
3. **Proximity Calculation:** Iterates over the matrix. When a mine is found, it uses **Direction Vectors** to increment the value of all 8 adjacent cells (provided they are within bounds and aren't mines themselves).

## Features
- **Direction Vectors (`dr, dc`):** Replaces verbose and repetitive `if` statements with a clean, pythonic loop over relative adjacent coordinates.
- **Robust Input Validation:** Uses `while/try/except` loops to prevent crashes from bad inputs (e.g., typing text instead of integers, or inputting out-of-bounds coordinates).

## How to Run
Execute the script in your terminal:
```bash
python main.py