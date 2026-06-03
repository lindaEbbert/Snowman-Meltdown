def get_single_letter_input():
    while True:
        user_input = input("Guess a letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        print("Please enter a single alphabetical character.")