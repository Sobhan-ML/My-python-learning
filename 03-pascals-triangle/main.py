def pascal(n):
    """Generates the n-th row of Pascal's Triangle using recursion."""
    if n == 1:
        return [1]

    prev = pascal(n - 1)
    row = [1]
    for j in range(len(prev) - 1):
        row.append(prev[j] + prev[j + 1])
    row.append(1)
    return row


def main():
    print("====================================")
    print("Welcome to Pascal's Triangle Generator! 📐")
    print("====================================")

    try:
        # User-friendly input message
        n = int(input("Enter the number of rows you want to generate: "))

        if n <= 0:
            print("❌ Please enter a positive number greater than 0.")
            return

        print("\nHere is your Pascal's Triangle:\n")
        for i in range(1, n + 1):
            # Using join to make the output look clean and separated by spaces
            row_str = " ".join(map(str, pascal(i)))
            print(row_str)

        print("\nExecution completed successfully! 🚀")

    except ValueError:
        print("❌ Invalid input! Please enter a valid whole number.")


if __name__ == "__main__":
    main()
