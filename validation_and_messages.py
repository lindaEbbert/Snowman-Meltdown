def get_single_letter_input():
    while True:
        user_input = input("Guess a letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        print("Please enter a single alphabetical character.")


def ask_if_user_wants_to_quit():
    while True:
        user_input = input("Another round? (y/n): ").lower()
        if user_input in ["y", "n"]:
            return user_input == "n"
        print("Please enter 'y' or 'n'.")


def reply_to_quit_request(user_wants_to_quit):
    if user_wants_to_quit:
        print("Thanks for playing!")
    else:
        print("Okay, let's play again!")