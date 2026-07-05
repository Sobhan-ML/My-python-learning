def is_armstrong(number):
    """Checks if a number is an Armstrong number."""
    num_str = str(number)
    power = len(num_str)
    # Using list comprehension and sum() for cleaner Pythonic code
    total = sum(int(digit) ** power for digit in num_str)
    return total == number


def main():
    print("========================================")
    print("Welcome to the Armstrong Number Finder! 🔢")
    print("========================================")

    # 1. Validation loop for getting the number of elements (n)
    while True:
        try:
            n = int(input("Enter the number of elements (n): "))
            if n <= 0:
                print("❌ Error: Please enter a positive number greater than 0.\n")
                continue
            break
        except ValueError:
            print("❌ Warning: Please enter a valid whole number!\n")

    # 2. Validation loop for getting individual numbers
    numbers = []
    print(f"\nEnter {n} numbers:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("❌ Warning: Please enter a valid whole number!\n")

    # 3. Calculate the sum of the product of elements
    total_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            total_sum += numbers[i] * numbers[j]

    end_interval = 2 * total_sum

    # 4. Search for Armstrong numbers in the specified interval
    print(
        f"\n-> Searching for Armstrong numbers between 100 and {end_interval}...\n")
    found_any = False

    for i in range(100, end_interval + 1):
        if is_armstrong(i):
            print(f"✨ Found: {i}")
            found_any = True

    if not found_any:
        print("No Armstrong numbers found in this range. 🔄")

    print("\nCalculation completed successfully! 🚀")


if __name__ == "__main__":
    main()
