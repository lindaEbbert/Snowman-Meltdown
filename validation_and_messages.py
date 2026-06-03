# ---- messages ----
WELCOME_MESSAGE = "\033[1m"+"\x1b[94mWelcome to Snowman Meltdown!\x1b[0m"+"\033[0m"
WINNING_MESSAGE = "\x1b[32mCongratulations! You saved the snowman!\x1b[0m"

def print_gameover_message(secret_word):
    """Prints a message indicating the game is over.
    :param secret_word: The secret word that the user should have guessed.
    """
    print(f"\x1b[31mGame over! The word was: {secret_word}")


# ---- input handling ----
def get_single_letter_input():
    """Returns a single alphabetical character entered by the user."""
    while True:
        user_input = input("\x1b[94mGuess a letter: \x1b[0m")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        print("\x1b[31mPlease enter a single alphabetical character.\x1b[0m")


def ask_if_user_wants_to_quit():
    """Returns True if the user wants to quit, False otherwise."""
    while True:
        user_input = input("\x1b[94m\nAnother round? (y/n): \x1b[0m").lower()
        if user_input in ["y", "n"]:
            return user_input == "n"
        print("\x1b[31mPlease enter 'y' or 'n'.\x1b[0m")


def reply_to_quit_request(user_wants_to_quit):
    """Prints a message depending on whether the user wants to quit or not.
    :param user_wants_to_quit: Boolean value indicating whether the user wants to quit.
    """
    if user_wants_to_quit:
        print("\x1b[94mThanks for playing!\x1b[0m")
    else:
        print("\x1b[94mOkay, let's play again!\n\x1b[0m")
        print("____________________________")
        print("____________________________")