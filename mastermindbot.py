import random
from itertools import product
from game_logic import check_guess


class MastermindBot:
    """
    A "bot" that helps generate smart guesses based on history of guess
    """

    def __init__(self, code_length, digit_min, digit_max):
        """
        Initialize the game with code length and digit range

            Args:
                code_length(int) = length of code
                digit_range(int) = range of digits to choose from
            """
        self.possible_codes = set(product(range(int(digit_min), int(digit_max)), repeat=code_length))

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

        if not self.possible_codes:
            return None
        
        for guess, feedback in history:
            if (tuple(guess),feedback) not in self.filtered_history:
                self.filter_possible_guesses(guess,feedback)
                self.filtered_history.add((tuple(guess),feedback))


        return random.choice(list(self.possible_codes))
    
    # def worst_case_score(self, guess):
    #     """
    #     Calculate the worst-case score for a potential guess.
        
    #     Args:
    #         guess (tuple[int]): A potential guess.
        
    #     Returns:
    #         int: The worst-case score for this guess.
    #     """
    #     score_map = {}
    #     for code in self.possible_codes:
    #         feedback = check_guess(code, list(guess))
    #         score_map[feedback] = score_map.get(feedback, 0) + 1 #  checks if feedback exists as a key in the dictionary score_map and if so adds it to the specific
    #     return max(score_map.values())

    # def get_hint_smarter(self, history):
    #     """
    #     Generate the best next guess using a more efficient strategy.
        
    #     Args:
    #         history (list[tuple[list[int], tuple[int, int]]]):
    #             Previous guesses and feedback pairs.
        
    #     Returns:
    #         list[int]: A new guess likely to be correct.
    #     """
    #     if not self.possible_codes:
    #         return None

    #     # Filter guesses based on previous feedback
    #     for guess, feedback in history:
    #         if (tuple(guess), feedback) not in self.filtered_history:
    #             self.filter_possible_guesses(guess, feedback)
    #             self.filtered_history.add((tuple(guess), feedback))

    #     # Use minimax strategy: Find the guess with the smallest maximum score
    #     best_guess = min(
    #         self.possible_codes, 
    #         key=lambda code: self.worst_case_score(code)
    #     )

    #     return list(best_guess)
