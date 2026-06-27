# Spiral Coordinates Finder

An algorithmic Python solution to find the exact Cartesian coordinates $(X, Y)$ of the $n$-th step in a rectangular spiral starting from the origin.

## Mathematical Logic
Instead of simulating the movement step-by-step (which would be slow and inefficient), this program uses a purely mathematical approach with $O(1)$ time complexity:
1. **Quotient ($q = n // 4$):** Determines the "layer" or the distance of the point from the center.
2. **Remainder ($r = n \% 4$):** Determines the specific corner or direction of the point on the current layer.

By matching the remainder to one of the four possible corners, the exact $(X, Y)$ position is instantly calculated.

## How to Run
Execute the script in your terminal:
```bash
python main.py