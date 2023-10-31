import random

secret_number = random.randint(1, 100)

for _ in range(3):
    guess = int(input("Guess the secret number (between 1 and 100): "))

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed the secret number ", secret_number)
        break
else:
    print("Sorry, you couldn't guess the secret number. It was ", secret_number)

