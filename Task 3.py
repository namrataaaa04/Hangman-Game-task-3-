import random

WORDS = ["python", "hangman", "developer", "keyboard", "internship"]
MAX_ERRORS = 6


def display(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)


def get_guess(seen):
    while True:
        guess = input("Letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter.")
        elif guess in seen:
            print("Already guessed.")
        else:
            return guess


def play():
    secret = random.choice(WORDS)
    guessed = set()
    errors = 0

    print("Hangman")
    while errors < MAX_ERRORS and not set(secret).issubset(guessed):
        print(display(secret, guessed))
        print(f"Errors: {errors}/{MAX_ERRORS}")
        guess = get_guess(guessed)
        guessed.add(guess)
        if guess not in secret:
            errors += 1
            print("Wrong.")
        else:
            print("Correct.")

    print(display(secret, guessed))
    if set(secret).issubset(guessed):
        print(f"You win! The word was {secret}.")
    else:
        print(f"You lose. The word was {secret}.")


if __name__ == "__main__":
    while input("Play again? (y/n): ").lower().strip() == "y":
        play()
        