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
    print("========================================")
    print("Welcome to Pascal's Triangle Generator! 📐")
    print("========================================")
    
    while True:
        try:
            n = int(input("Enter the number of rows you want to generate: "))
            
            if n <= 0:
                print("❌ Please enter a positive number greater than 0.\n")
                continue 
                
            print("\nHere is your Pascal's Triangle:\n")
            for i in range(1, n + 1):
                row_str = " ".join(map(str, pascal(i)))
                print(row_str)
                
            print("\nExecution completed successfully! 🚀")
            break 
            
        except ValueError:
            print("❌ Warning: Invalid input! Please enter a valid whole number.\n")


if __name__ == "__main__":
    main()