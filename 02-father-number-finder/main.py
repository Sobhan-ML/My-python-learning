def precompute_fathers(max_limit):
    """Precomputes which numbers have a 'father' using an efficient Sieve method."""
    prime_sum = [0] * max_limit
    for i in range(2, max_limit):
        if prime_sum[i] == 0:
            for j in range(i, max_limit, i):
                prime_sum[j] += i

    has_father = [False] * max_limit
    for x in range(1, max_limit):
        digit_sum = sum(int(digit) for digit in str(x))
        dx = x + prime_sum[x] + digit_sum
        if dx < max_limit:
            has_father[dx] = True
    return has_father


def main():
    MAX_LIMIT = 100005
    
    print("====================================")
    print("Welcome to the Father Number Finder! ✨")
    print("====================================")
    print("Initializing the mathematical engine, please wait...")
    
    has_father = precompute_fathers(MAX_LIMIT)
    print("Engine ready!\n")

    while True:
        try:
            test_cases = int(input("How many numbers do you want to check today? "))
            if test_cases <= 0:
                print("❌ Please enter a positive number greater than 0.\n")
                continue
            break 
        except ValueError:
            print("❌ Warning: Please enter a valid number, not text!\n")

    print("-" * 40)

    for i in range(test_cases):
        while True:
            try:
                n = int(input(f"[{i + 1}] Enter a number (0 to {MAX_LIMIT - 6}): "))
                
                if 0 <= n < MAX_LIMIT:
                    if has_father[n]:
                        print(f"-> Result: Yes, {n} has a father number!\n")
                    else:
                        print(f"-> Result: No, {n} does not have a father number.\n")
                    break 
                else:
                    print(f"❌ Error: Please enter a number between 0 and {MAX_LIMIT - 6}.\n")
                    
            except ValueError:
                print("❌ Warning: Invalid input! Please enter a whole number.\n")
                
    print("Thanks for playing! Happy coding! 🚀")


if __name__ == "__main__":
    main()