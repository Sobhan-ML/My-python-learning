def is_prime(x):
    """Checks if a number is prime using square root optimization."""
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def main():
    print("========================================")
    print("Welcome to the Super Prime Finder! 🔢")
    print("========================================")

    while True:
        try:
            n = int(
                input("Enter the position (n) of the super prime you want to find: "))

            if n <= 0:
                print("❌ Error: Please enter a positive number greater than 0.\n")
                continue
            break

        except ValueError:
            print("❌ Warning: Please enter a valid whole number, not text!\n")

    super_primes = [2, 3, 5, 7]

    if n <= 4:
        print(
            f"\n-> Result: The super prime at position {n} is {super_primes[n - 1]} 🚀")
    else:
        count = 4
        i = 0
        while count < n:
            current = super_primes[i]
            i += 1

            for digit in [1, 3, 7, 9]:
                new_num = current * 10 + digit

                if is_prime(new_num):
                    super_primes.append(new_num)
                    count += 1

                    if count == n:
                        print(
                            f"\n-> Result: The super prime at position {n} is {new_num} 🚀")
                        break

            if count == n:
                break


if __name__ == "__main__":
    main()
