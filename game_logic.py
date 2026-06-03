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
