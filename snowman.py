from ascii_art import STAGES
from game_logic import get_random_word, display_game_state, get_word_state
from validation_and_messages import get_single_letter_input, ask_if_user_wants_to_quit, reply_to_quit_request, \
    print_gameover_message
from validation_and_messages import WELCOME_MESSAGE, WINNING_MESSAGE


def play_game():
    user_wants_to_quit = False
    print(WELCOME_MESSAGE)

    while not user_wants_to_quit:
        secret_word = get_random_word()
        mistakes = 0
        max_mistakes = len(STAGES) - 1
        guessed_letters = []

        while mistakes < max_mistakes:
            guess = get_single_letter_input().lower()
            if guess not in secret_word:
                mistakes += 1
            else:
                guessed_letters.append(guess)
            display_game_state(mistakes, secret_word, guessed_letters)
            word_is_complete = "_" not in get_word_state(secret_word, guessed_letters)
            if word_is_complete:
                print(WINNING_MESSAGE)
                user_wants_to_quit = ask_if_user_wants_to_quit()
                reply_to_quit_request(user_wants_to_quit)
                break
        if mistakes == max_mistakes:
            print_gameover_message(secret_word)
            user_wants_to_quit = ask_if_user_wants_to_quit()
            reply_to_quit_request(user_wants_to_quit)


if __name__ == "__main__":
    play_game()