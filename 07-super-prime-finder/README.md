# Super Prime Finder 🔢

A Python command-line utility that calculates the n-th "Super Prime" (also known as a right-truncatable prime). A right-truncatable prime is a prime number that remains prime when the last rightmost digit is successively removed.

## How It Works
1. **Optimized Primality Test:** The program uses a square root optimization method (`O(sqrt(n))`) to check if a number is prime, making it extremely fast.
2. **Queue-Based Generation (BFS):** Starting with the base primes `[2, 3, 5, 7]`, the algorithm dynamically generates new primes by appending valid odd digits `[1, 3, 7, 9]` to the right side of existing super primes. It avoids generating non-primes by excluding even numbers and `5` as appending digits.
3. **Input Validation:** Built-in `try/except` loop ensures the program won't crash if the user inputs invalid data types (e.g., text or symbols).

## Features
- **Dynamic Calculation:** Can calculate deep into the sequence without pre-generating all numbers.
- **Robust Error Handling:** Keeps prompting until a valid positive integer is provided.

## How to Run
Execute the script in your terminal:
```bash
python main.py