import random

# Generate a random number between 1 and 99
secret_number = random.randint(1, 99)

print("Welcome to the Number Guessing Game!")

while True:
    try:
        # Get the user's guess
        guess = input("What is your number (1-99)? ")
        guess = int(guess)
    except ValueError:
        print("❌ Warning: Please enter a valid number, not text!\n")
        continue

    # Check the guess against the secret number
    if guess == secret_number:
        print("Wow! You did it! Congratulations! 🎉")
        break  # This stops the loop when the answer is correct
    elif guess > secret_number:
        print("Mine is smaller.")
    else:
        print("Mine is bigger.")