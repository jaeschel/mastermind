import random
from itertools import product
from game_logic import check_guess


class MastermindBot:
    """
    A "bot" that helps generate smart guesses based on history of guess
    """

    def __init__(self, code_length, digit_range):
        """
        Initialize the game with code length and digit range

            Args:
                code_length(int) = length of code
                digit_range(int) = range of digits to choose from
            """
        self.possible_codes = set(product(range(digit_range),
                                           repeat=code_length))
        self.filtered_history = set()

    def filter_possible_guesses(self, guess, feedback):
        """
        Parse through and keep only possible guesses
            Args:
                guess(list[int]) = a list of integers
                feeedback(tuple(int)) = a tuple of integers
                    ["Correct Positons", Right Number, Wrong Positon"]

            Returns:
                List[list] = a list of all remaining possible codes
                            ex = "[[1,2,3,4],[5,6,7,0]]"
        """
        self.possible_codes = {
            code for code in self.possible_codes
            if check_guess(code, guess) == feedback
        }

    def get_hint(self, history):
        """
        Generate a hint by removing impossible guesses and random selection
            SIMULATION:
                digit_range = 7, code_length = 5, n = 100
                Success Rate < 6 guesses
        """
        # if not history[-1][0]:  # check if we only have one entry
        #     self.filter_possible_guesses(history[0][0], history[0][1])
        # else:
        #     self.filter_possible_guesses(history[-1][0], history[-1][1])

        if not self.possible_codes:
            return None
        
        for guess, feedback in history:
            if (tuple(guess),feedback) not in self.filtered_history:
                self.filter_possible_guesses(guess,feedback)
                self.filtered_history.add((tuple(guess),feedback))


        return random.choice(list(self.possible_codes))
