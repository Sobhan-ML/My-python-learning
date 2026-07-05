# Armstrong Number Finder 🔢

A Python application that calculates a specific mathematical interval based on user input and searches for **Armstrong numbers** within that range. 

An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## Logic & Workflow
1. **Input Collection:** The user specifies the number of elements (`n`) and then inputs `n` integers.
2. **Interval Calculation:** The program calculates the sum of the products of all unique pairs in the provided list. The search interval is set from `100` up to `2 * total_sum`.
3. **Armstrong Verification:** It iterates through the calculated interval, checking each number against the Armstrong mathematical condition.

## Features
- **Clean Architecture:** Uses Pythonic methods like `sum()` and list comprehensions for optimal mathematical calculations.
- **Robust Input Validation:** Implements continuous `while/try/except` loops to prevent application crashes from invalid or non-integer inputs.

## How to Run
Execute the script in your terminal:
```bash
python main.py