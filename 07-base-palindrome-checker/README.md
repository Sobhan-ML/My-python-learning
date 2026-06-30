# Base Palindrome Checker 🔢

A Python utility that converts a number from a given base (`b`) to base 10, and then determines if its representation in a new target base (`c`) is a palindrome.

## Logic
1. **Base Conversion (Base B -> 10):** The program treats the input number as a sequence of digits and converts it using positional notation.
2. **Palindrome Check (Base 10 -> C):** The program repeatedly divides the number by the target base `c` to find the remainders (digits in base `c`). It then checks if the resulting string is a palindrome by comparing it to its reverse slice `[::-1]`.

## Features
- **Mathematical Validation:** Handles base conversion logic using integer arithmetic.
- **Robustness:** Includes `try/except` blocks to handle non-integer inputs gracefully, preventing crashes.

## How to Run
Execute the script in your terminal:
```bash
python main.py