# Masked Equation Solver 🧮

A Python utility that determines the missing digits in a simple addition equation string. Missing digits are represented by the `#` wildcard.

## Logic & Workflow
1. **Parsing:** The program splits the user's input string assuming the standard format `A + B = C`.
2. **Algebraic Calculation:** It identifies which component (A, B, or C) contains the `#` wildcard and calculates what its actual integer value *should* be based on the other two numbers.
3. **Regex Pattern Matching:** It converts the masked string (e.g., `1#`) into a Regular Expression pattern (e.g., `^1\d*$`) and verifies if the algebraically calculated value fits that pattern.

## Features
- **Regex Integration:** Utilizes Python's `re` module for flexible pattern matching.
- **Fault Tolerance:** Includes internal `try/except` blocks to catch `ValueError` exceptions if the user inputs multiple masked strings or malformed syntax.
- **Interactive CLI:** Runs a continuous `while` loop interface, allowing users to test multiple equations rapidly without restarting the script.

## How to Run
Execute the script in your terminal:
```bash
python main.py