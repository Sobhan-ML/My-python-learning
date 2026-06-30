def convert_to_decimal(number, base):
    """Converts a number (as digits) from a given base to decimal (base 10)."""
    temp_number = number
    number_str = str(number)
    total = 0

    for i in range(len(number_str)):
        # Extracting digits and converting based on positional value
        total += (temp_number % 10) * (base ** i)
        temp_number = temp_number // 10
    return total


def is_palindrome_in_base(number, target_base):
    """Checks if the representation of a number is a palindrome in a specific target base."""
    temp_number = number
    result_str = ''

    while True:
        if temp_number == 0:
            break
        result_str += str(temp_number % target_base)
        temp_number = temp_number // target_base

    # Check if the generated string is the same as its reverse
    return result_str == result_str[::-1]


def main():
    print("========================================")
    print("Welcome to the Base Palindrome Checker! 🔢")
    print("========================================")

    while True:
        try:
            # Inputs
            num_input = int(input("Enter the number (a): "))
            base_input = int(input("Enter the original base (b): "))
            target_base_input = int(input("Enter the target base (c): "))

            if base_input <= 1 or target_base_input <= 1:
                print("❌ Error: Bases must be greater than 1.\n")
                continue
            break

        except ValueError:
            print("❌ Warning: Please enter valid whole numbers!\n")

    # Processing
    decimal_value = convert_to_decimal(num_input, base_input)

    if is_palindrome_in_base(decimal_value, target_base_input):
        print("\n-> Result: YES, it's a palindrome in the new base! ✨")
    else:
        print("\n-> Result: NO, it's not a palindrome. 🔄")

    print("\nCalculation completed successfully! 🚀")


if __name__ == "__main__":
    main()
