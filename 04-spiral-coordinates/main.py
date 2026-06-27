def get_spiral_coordinates(n):
    """Calculates the (x, y) coordinates of the n-th point in a rectangular spiral."""
    q = n // 4
    r = n % 4
    
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
    
    while True:
        try:
            n = int(input("Enter the step number (n) to find its coordinates: "))
            
            if n < 0:
                print("❌ Please enter a positive integer.\n")
                continue
            
            x, y = get_spiral_coordinates(n)
            print(f"\n📍 The coordinates for step {n} are: (X: {x}, Y: {y})")
            print("\nExecution completed successfully! 🚀")
            break
            
        except ValueError:
            print("❌ Warning: Invalid input! Please enter a valid whole number.\n")


if __name__ == "__main__":
    main()
