def precompute_fathers(max_limit):
    """Precomputes which numbers have a 'father' using an efficient Sieve method."""
    # 1. Precompute the sum of prime factors
    prime_sum = [0] * max_limit
    for i in range(2, max_limit):
        if prime_sum[i] == 0:  # i is a prime number
            for j in range(i, max_limit, i):
                prime_sum[j] += i

    # 2. Track if a number has a father
    has_father = [False] * max_limit

    for x in range(1, max_limit):
        digit_sum = sum(int(digit) for digit in str(x))
        dx = x + prime_sum[x] + digit_sum

        if dx < max_limit:
            has_father[dx] = True

    return has_father


def main():
    MAX_LIMIT = 100005

    print("Welcome to the Father Number Finder!")
    print("Initializing the mathematical engine, please wait...")

    # Precompute data so the lookups are instant
    has_father = precompute_fathers(MAX_LIMIT)

    print("Engine ready! ✨\n")

    try:
        # Ask the user for the number of rounds
        test_cases = int(
            input("How many numbers do you want to check today? "))
        print("-" * 40)

        for i in range(test_cases):
            n = int(input(f"[{i + 1}] Enter a number (up to 100,000): "))

            # Check the precomputed table
            if 0 <= n < MAX_LIMIT:
                if has_father[n]:
                    print(f"-> Result: Yes, {n} has a father number!\n")
                else:
                    print(
                        f"-> Result: No, {n} does not have a father number.\n")
            else:
                print(
                    f"-> Error: Please enter a number between 0 and {MAX_LIMIT - 5}.\n")

        print("Thanks for playing! Happy coding! 🚀")

    except ValueError:
        print("Invalid input! Please enter whole numbers only.")


if __name__ == "__main__":
    main()
