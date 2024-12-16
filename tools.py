import re
from game_settings import GameSettings

settings = GameSettings()


def validate_input(guess, code_length, digit_range_min, digit_range_max):
    """
    Validates user guess within game restraints

    Args:
        guess (list[int]): The user's guessed numbers.
        code_length (int): The required length of the guess.
        digit_range (int): The maximum allowable digit value (exclusive).
    
    Returns:
        list[int]: The validated guess if it meets all constraints, 
                   or an empty list if the input is invalid.
    """
    if str(guess).strip().lower() == 'hint':
        return(guess)

    if guess and len(guess) == code_length and all(digit_range_min <= n < digit_range_max for n in guess):
        return(guess)
    
    else:
        print(f"\nInvalid input. Enter exactly {code_length} numbers from {digit_range_min} to {digit_range_max-1}.")
        return []


def cleanup_guess(guess):
    """
    Clean up input to allow for spaces, commas and brackets

        Args:
            guess(str) - A string input from user.

        Returns:
            List[intdoe]: a cleaned list of integers.
    """
    if not isinstance(guess, str):
        return []
    # Using re.findall to find digits in guess and return them
    # Cleaning up input to only integers
    elif guess.strip().lower() == 'hint':
        return guess.strip().lower()
    else:
        cleaned_guess = re.findall(r'\d', guess)
        return list(map(int, cleaned_guess))


def get_user_guess(hint_used, code_length, digit_range_min, digit_range_max):
    """
    Prompts the user to enter a guess and validates the input.

    Args:
        hint_used (bool): Whether the user has already used a hint.
        code_length (int): The required length of the guess.
        digit_range (int): The maximum allowable digit value (exclusive).

    Returns:
        list[int]: The validated user guess if input is valid, 
                   or an empty list if the input is invalid.
    """

    prompt = f"\nEnter your {code_length} number guess"
    if hint_used:
        prompt += "! You've already used a hint this round. : "
    else:
        prompt += " or 'hint' for a hint! : "

    guess = cleanup_guess(input(prompt))
    guess = validate_input(guess, code_length, digit_range_min, digit_range_max)

    return guess

def display_guess_history(history):
    """
    Prints the guess history along with the evalutaion

        Args:
            history(list[tuple]) = a list of all guesses and their evaluations

    """

    print("Guess History")

    for index, (guessed_code, (correct_pos, correct_num)) in enumerate(history, 1):
        # starting at 1, loop and unpack the entire history list

        print(f"Guessed Code #{index} :  {guessed_code}")
        print(f"   Right Positions: {correct_pos}")
        print(f"   Right Number, Wrong positions: {correct_num}")
