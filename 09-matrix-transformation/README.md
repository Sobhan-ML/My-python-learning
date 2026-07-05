# Matrix Image Transformer 🖼️

A Python command-line utility that performs 2D matrix transformations, simulating basic image manipulation operations like rotation and mirroring.

## Supported Operations
- **`90`**: Rotates the matrix 90 degrees clockwise.
- **`H`**: Flips the matrix vertically (upside down) across the horizontal axis.
- **`V`**: Flips the matrix horizontally (left to right) across the vertical axis.

## Features
- **Efficient Slicing:** Utilizes Python's highly optimized native slicing (`[::-1]`) for instant matrix mirroring.
- **Clean Architecture:** Separates transformation logic into clear, single-responsibility English functions (`rotate_90_clockwise`, `flip_horizontally`, `flip_vertically`).
- **Robust Wrapper:** Out-of-the-box `try/except` block protecting the program from crashing due to unexpected non-integer inputs.

## How to Run
Run the script via terminal:
```bash
python main.py