import random

def generate_random_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "In order to be irreplaceable, one must always be different.",
        "Experience is the name everyone gives to their mistakes.",
        "Java is to JavaScript what car is to carpet.",
        "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code."
    ]
    return random.choice(quotes)

def random_number_game():
    print("Welcome to the Random Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("Here's a random programming quote for you:")
    print(generate_random_quote())
    print()
    random_number_game()