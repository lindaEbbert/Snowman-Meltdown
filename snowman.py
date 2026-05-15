import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_snowman_stage(mistakes):
    """Returns the current stage of the snowman based on the number of mistakes."""
    return STAGES[mistakes]


def get_word_state(secret_word, guessed_letters):
    """Returns the current state of the word, with guessed letters added."""
    word_state = ""
    for letter in secret_word:
        if letter in guessed_letters:
            word_state += letter + " "
        else:
            word_state += "_ "
    return word_state


def display_game_state(mistakes, secret_word, guessed_letters):
    """Prints the current state of the game to the console."""
    print(get_snowman_stage(mistakes)+"\n")
    print(f"Word: {get_word_state(secret_word, guessed_letters)}\n")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    mistakes = 0
    max_mistakes = len(STAGES) - 1
    guessed_letters = []

    while mistakes < max_mistakes:
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        if guess not in secret_word:
            mistakes += 1
        else:
            guessed_letters.append(guess)
        display_game_state(mistakes, secret_word, guessed_letters)
        #if len(guessed_letters) != 0:
        word_is_complete = "_" not in get_word_state(secret_word, guessed_letters)
        if word_is_complete:
            print("Congratulations! You saved the snowman!")
            break
    if mistakes == max_mistakes:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    play_game()