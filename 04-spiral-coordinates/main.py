def get_spiral_coordinates(n):
    """Calculates the (x, y) coordinates of the n-th point in a rectangular spiral."""
    q = n // 4
    r = n % 4

    # Determine the coordinates based on the remainder (corner direction)
    if r == 0:
        return -q, q
    elif r == 1:
        return -q, -q
    elif r == 2:
        return q + 1, -q
    else:
        return q + 1, q + 1


def main():
    print("=========================================")
    print("Welcome to the Spiral Coordinates Finder! 🌀")
    print("=========================================")

    try:
        n = int(input("Enter the step number (n) to find its coordinates: "))

        if n < 0:
            print("❌ Please enter a positive integer.")
            return

        x, y = get_spiral_coordinates(n)
        print(f"\n📍 The coordinates for step {n} are: (X: {x}, Y: {y})")
        print("\nExecution completed successfully! 🚀")

    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number.")


if __name__ == "__main__":
    main()
