# Father Number Finder

An interactive and highly optimized Python application that solves an interesting mathematical puzzle: determining if a number has a "father" (generator) number.

## The Math Puzzle
A number $x$ is considered the "father" of a number $n$ if you can get $n$ by adding $x$ to the sum of its prime factors and the sum of its digits:

$$d(x) = x + \text{sum\_of\_prime\_factors}(x) + \text{sum\_of\_digits}(x) = n$$

This program instantly checks if any given number $n$ has such a generator.

## Key Features & Optimizations
- Interactive CLI: A friendly command-line interface that guides the user through inputs.
- Sieve of Eratosthenes: Instead of slow, repetitive calculations, it uses an optimized Sieve method to precompute the sum of prime factors for all numbers up to $10^5$.
- Instant Lookups: Thanks to the precomputation table, checking each number takes $O(1)$ time complexity, providing split-second responses.

## How to Run & Use
1. Clone the repository or navigate to this folder.
2. Run the script using Python:
   `bash
   python main.py