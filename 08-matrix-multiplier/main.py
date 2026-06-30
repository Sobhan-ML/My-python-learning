def main():
    print("========================================")
    print("Welcome to the Matrix Multiplier! ✖️")
    print("========================================")

    try:
        # Get dimensions
        print(
            "Enter dimensions (Rows of A, Common Dimension, Cols of B) separated by space:")
        rows_a, common_dim, cols_b = map(int, input("-> ").split())

        # Get Matrix A
        print(
            f"\nEnter the {rows_a} rows for Matrix A (each row should have {common_dim} numbers):")
        matrix_a = []
        for _ in range(rows_a):
            row = list(map(int, input().split()))
            matrix_a.append(row)

        # Get Matrix B
        print(
            f"\nEnter the {common_dim} rows for Matrix B (each row should have {cols_b} numbers):")
        matrix_b = []
        for _ in range(common_dim):
            row = list(map(int, input().split()))
            matrix_b.append(row)

        # Initialize the result matrix with zeros using list comprehension
        result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

        # Core Matrix Multiplication Logic (O(N^3) Time Complexity)
        for i in range(rows_a):
            for k in range(cols_b):
                for t in range(common_dim):
                    result_matrix[i][k] += matrix_a[i][t] * matrix_b[t][k]

        # Print the resulting matrix
        print("\n-> Resulting Matrix:")
        for row in result_matrix:
            print(*row)

    except ValueError:
        print("\n❌ Error: Invalid input. Please make sure to enter only integers separated by spaces.")
    except IndexError:
        print("\n❌ Error: The dimensions provided do not match the number of elements entered in the rows.")


if __name__ == "__main__":
    main()
