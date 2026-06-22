import random

# The computer picks a random number
secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

# Start the game loop
while True:
    guess = int(input("Enter your guess:"))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the secret number!")
        break
