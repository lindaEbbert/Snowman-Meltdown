# ---- messages ----
WELCOME_MESSAGE = "\033[1m"+"\x1b[94mWelcome to Snowman Meltdown!\x1b[0m"+"\033[0m"
WINNING_MESSAGE = "\x1b[32mCongratulations! You saved the snowman!\x1b[0m"

def print_gameover_message(secret_word):
    print(f"\x1b[31mGame over! The word was: {secret_word}")


# ---- input handling ----
def get_single_letter_input():
    while True:
        user_input = input("\x1b[94mGuess a letter: \x1b[0m")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        print("\x1b[31mPlease enter a single alphabetical character.\x1b[0m")


def ask_if_user_wants_to_quit():
    while True:
        user_input = input("\x1b[94m\nAnother round? (y/n): \x1b[0m").lower()
        if user_input in ["y", "n"]:
            return user_input == "n"
        print("\x1b[31mPlease enter 'y' or 'n'.\x1b[0m")


def reply_to_quit_request(user_wants_to_quit):
    if user_wants_to_quit:
        print("\x1b[94mThanks for playing!\x1b[0m")
    else:
        print("\x1b[94mOkay, let's play again!\n\x1b[0m")
        print("____________________________")
        print("____________________________")