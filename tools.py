import re

def cleanup_input(guess):
    """
    Clean up input to allow for spaces, commas and brackets

        Args:
            guess(str) - A string input from user

        Returns:
            List[intdoe]: a cleaned list of integers.
    """
    if not isinstance(guess,str):
        return []
    # Using re, findall digits in guess and return those characters
    # Cleaning up input to only integers 
    cleaned_guess = re.findall(r'\d', guess)
    return list(map(int,cleaned_guess))

def display_guess_history(history):
    """
    Prints the guess history along with the evalutaion

        Args:
            history(list[tuple]) = a list of all the guesses and their evaluations
    
    """

    print("Guess History")

    for index, (guessed_code, (correct_pos, correct_num)) in enumerate(history, 1):
    # starting at 1, loop and unpack the entire history list
        print (f"\nGuessed Code #{index} :  {guessed_code}")
        print (f"   Right Positions: {correct_pos}")
        print (f"   Right Number, Wrong positions: {correct_num}")


