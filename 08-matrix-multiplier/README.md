# Matrix Multiplier ✖️

A Python command-line application that performs mathematical matrix multiplication for two matrices of custom dimensions. 

## How It Works
The program follows the standard algebraic rule for matrix multiplication:
1. It takes three dimensions: `Rows of A`, `Common Dimension` (Cols of A / Rows of B), and `Cols of B`.
2. It accepts the elements for **Matrix A** and **Matrix B** row by row.
3. It initializes a result matrix with zeros using Python's list comprehension.
4. It calculates the dot product of rows and columns using a classic 3-nested-loop algorithm.

## Features
- **Algorithmic Implementation:** Accurately implements the $O(n^3)$ time complexity matrix multiplication algorithm.
- **Clean Code:** Uses descriptive English variable names (`rows_a`, `common_dim`, `matrix_a`) instead of ambiguous single-letter variables for maximum readability.
- **Error Handling:** Built-in `try/except` blocks gracefully handle `ValueError` (if the user types letters instead of numbers) and `IndexError` (if the row length doesn't match the defined dimensions).

## How to Run
Execute the script in your terminal and follow the prompts:
```bash
python main.py