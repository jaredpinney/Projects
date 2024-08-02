import random

def _get_input(prompt_text = "Your guess please: ", min=1, max=100):
    """prompts for input, validates input, returns sanitized data"""
    # Keep looping until passes validation and returns.
    # First convert to int. if not int, print message and restart loop
    # Then do a range check. if in range, return the variable, else print a message (and loop will restart)
    while True:
        s = input(prompt_text)
        try:
            s = int(s)
        except: 
            print("Your input is non-numeric...")
            continue
        if s >= min and s <= max:
            return s
        else:
            print("Your input is out of range, can't you read?")

def create_number_guesser():
    """interactive number guessing game"""

    print("Guess a number between 1 and 100. I will tell you if the number I chose is lower or higher than your guess..")

    rand_number = random.randint(1, 100)
    guess = None

    while rand_number != guess:
        guess = _get_input() 
        if rand_number > guess:
            print("Higher")
        elif rand_number < guess:
            print("Lower")
        else:
            print("You guessed the random number of {}! Well I'll be damned, I was really starting to think you were stupid.".format(rand_number))

if __name__ == '__main__':

    create_number_guesser()