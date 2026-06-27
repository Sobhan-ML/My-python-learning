# Square Frame Generator 🔲

A Python command-line program that dynamically generates and prints a symmetric hollow square (a frame) using asterisks (`*`) based on user-defined dimensions.

## How It Works
The program asks the user for two inputs:
1. **`a`**: The size of the outer square.
2. **`b`**: The size of the inner hole.

It then calculates the padding and draws the frame. To ensure the frame is perfectly symmetric, the program uses a clever mathematical logic:
- The outer size (`a`) must be strictly greater than the inner size (`b`).
- The difference between `a` and `b` (`c = a - b`) **must be an even number**. This guarantees equal padding on all sides.

## Features
- **Mathematical Validation:** Automatically checks if the inputs can form a symmetric frame before attempting to draw it.
- **Robust Input Handling:** Uses a `while True` loop and `try/except` blocks to prevent the program from crashing if the user accidentally enters text instead of numbers.
- **Clean Output:** Uses Python's `.join()` method for clean and efficient string formatting.

## How to Run
Execute the script in your terminal:
```bash
python main.py