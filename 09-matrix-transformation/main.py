def rotate_90_clockwise(matrix, size):
    """Rotates an n x n matrix 90 degrees clockwise."""
    rotated_matrix = []
    for col in range(size):
        new_row = []
        for row in range(size - 1, -1, -1):
            new_row.append(matrix[row][col])
        rotated_matrix.append(new_row)
    return rotated_matrix


def flip_horizontally(matrix):
    """Flips the matrix horizontally (left to right swap)."""
    flipped_matrix = []
    for row in matrix:
        flipped_matrix.append(row[::-1])
    return flipped_matrix


def flip_vertically(matrix):
    """Flips the matrix vertically (upside down swap)."""
    return matrix[::-1]


def main():
    print("========================================")
    print("Welcome to the Matrix Transformer! 🖼️")
    print("========================================")

    while True:
        try:
            n = int(input("Enter matrix size (n): "))
            if n <= 0:
                print("❌ Error: Matrix size must be greater than 0.\n")
                continue
            break
        except ValueError:
            print("❌ Warning: Please enter a valid whole number for size!\n")

    print(f"Enter the {n} rows of the matrix:")
    matrix = []
    for _ in range(n):
        row = list(input())
        matrix.append(row)

    while True:
        try:
            q = int(input("Enter the number of operations (q): "))
            if q < 0:
                print("❌ Error: Operations count cannot be negative.\n")
                continue
            break
        except ValueError:
            print("❌ Warning: Please enter a valid whole number for operations count!\n")

    print("Enter the operations ('90' for rotation, 'H' for horizontal flip, 'V' for vertical flip):")
    current_matrix = matrix
    for i in range(q):
        operation = input(f"Op {i+1}: ").strip()

        if operation == '90':
            current_matrix = rotate_90_clockwise(current_matrix, n)
        elif operation == 'H':
            # Reversing rows sequence is a vertical flip
            current_matrix = flip_vertically(current_matrix)
        elif operation == 'V':
            # Reversing elements inside rows is a horizontal flip
            current_matrix = flip_horizontally(current_matrix)
        else:
            print(f"⚠️ Unknown operation '{operation}', skipped.")

    # Print the final transformed matrix
    print("\n-> Transformed Matrix:")
    for row in current_matrix:
        print(''.join(row))


if __name__ == "__main__":
    main()
