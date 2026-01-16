import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val:
        if user_input is 'l':
            return True
    else:
        if user_input is 'h':
            return True
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    pass
