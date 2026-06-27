def main():
    print("========================================")
    print("Welcome to the Square Frame Generator! 🔲")
    print("========================================")

    while True:
        try:
            a = int(input("Enter the outer square size (a): "))
            b = int(input("Enter the inner hole size (b): "))

            c = a - b

            if b >= a:
                print(
                    "❌ Error: 'Wrong order!' The outer size must be greater than the inner size.\n")
                continue
            elif c % 2 != 0:
                print(
                    "❌ Error: 'Wrong difference!' The difference between 'a' and 'b' must be an even number to keep it symmetric.\n")
                continue
            else:
                break

        except ValueError:
            print("❌ Warning: Please enter valid whole numbers, not text!\n")

    print("\nHere is your frame:\n")
    pad = c // 2

    for i in range(1, a + 1):
        if i <= pad or i > a - pad:
            row = ["*"] * a
            print(" ".join(row))
        else:
            row = ["*"] * pad + [" "] * b + ["*"] * pad
            print(" ".join(row))

    print("\nFrame generated successfully! 🚀")


if __name__ == "__main__":
    main()
