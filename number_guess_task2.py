import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100.")
    
    while True:
        # Prompt the user to input their guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the right number.")
            break

# Start the game
guess_the_number()
