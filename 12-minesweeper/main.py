def generate_minesweeper_board(rows, cols, mines):
    """
    Generates a Minesweeper board given dimensions and a list of mine coordinates.
    """
    # Initialize board with zeros using list comprehension
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Place mines on the board
    for r, c in mines:
        board[r][c] = '*'

    # Standard engineering trick: Direction vectors for 8 adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # Calculate adjacent mine counts
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '*':
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    # Check boundaries and ensure the adjacent cell is not a mine
                    if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != '*':
                        board[ni][nj] += 1

    return board


def main():
    print("========================================")
    print("Welcome to the Minesweeper Generator! 💣")
    print("========================================")

    # 1. Validation loop for board dimensions
    while True:
        try:
            rows, cols = map(int, input(
                "Enter board dimensions (rows cols): ").split())
            if rows <= 0 or cols <= 0:
                print("❌ Error: Dimensions must be greater than 0.\n")
                continue
            break
        except ValueError:
            print("❌ Warning: Please enter two valid integers separated by a space!\n")

    # 2. Validation loop for number of mines
    while True:
        try:
            mines_count = int(input("Enter the number of mines (k): "))
            if mines_count < 0 or mines_count > rows * cols:
                print(
                    f"❌ Error: Invalid number of mines. Must be between 0 and {rows * cols}.\n")
                continue
            break
        except ValueError:
            print("❌ Warning: Please enter a valid whole number!\n")

    # 3. Validation loop for mine coordinates
    mines = []
    if mines_count > 0:
        print(
            f"\nEnter the coordinates for {mines_count} mines (row col, 1-indexed):")

    for i in range(mines_count):
        while True:
            try:
                r, c = map(int, input(f"Mine {i + 1}: ").split())
                if not (1 <= r <= rows) or not (1 <= c <= cols):
                    print(
                        f"❌ Error: Coordinates must be within grid (1 to {rows}, 1 to {cols}).\n")
                    continue

                # Convert 1-indexed user input to 0-indexed for Python lists
                mines.append((r - 1, c - 1))
                break
            except ValueError:
                print(
                    "❌ Warning: Please enter two valid integers separated by a space!\n")

    # Generate and print the board
    board = generate_minesweeper_board(rows, cols, mines)

    print("\n-> Generated Board:")
    for row in board:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
