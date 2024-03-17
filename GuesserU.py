import random

def runGame():
    print(GREEN + "Welcome to the guessing game!" + RESET)

    # Validate user input is int
    while(True):
        user_input = input(f"{YELLOW}Please enter a max number: {RESET}")
        if user_input.isdigit():
            max = int(user_input)
            break
        else:
            print(RED + "Input is not an integer." + RESET)

    target = random.randrange(1, max)
    while(True):
        while(True):
            user_input = input(f"{BLUE}Enter a number between 1 - {max}: {RESET}")
            if user_input.isdigit():
                guess = int(user_input)
                break
            else:
                print(RED + "Input is not an integer." + RESET)
        if guess == target:
            print(GREEN + "Congrats! You guessed the correct number!")
            print("Thanks for playing!")
            break
        else:
            print(RED + "Not quite..." + RESET)
            if guess < target:
                print(LAVENDER + "(Number is higher!)" + RESET)
            else:
                print(LAVENDER + "(Number is lower!)" + RESET)

# Colors!
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
LAVENDER = '\033[38;2;230;200;250m'
RESET = '\033[0m'

# Run game!
runGame()


# Change