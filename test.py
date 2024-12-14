import unittest
from unittest.mock import patch
from game_logic import check_guess, generate_secret_code
from tools import cleanup_input, display_guess_history
from game_settings import GameSettings
from mastermindbot import MastermindBot

class TestMastermindEdgeCases(unittest.TestCase):

    def report(self, test_name, passed):
        if passed:
            print(f".[✔] {test_name} PASSED")
        else:
            print(f".[✘] {test_name} FAILED")

    @patch("builtins.input", side_effect=["1", "2"])
    def test_minimal_game_settings(self, mock_input):
        settings = GameSettings()
        result = settings.configure()
        self.report("test_minimal_game_settings", result == (1, 2))

    def test_check_guess_all_same_digits(self):
        secret_code = [7, 7, 7, 7]
        guess = [7, 7, 7, 7]
        result = check_guess(secret_code, guess)
        self.report("test_check_guess_all_same_digits", result == (4, 0))

    def test_check_guess_all_incorrect(self):
        secret_code = [0, 1, 2, 3]
        guess = [4, 5, 6, 7]
        result = check_guess(secret_code, guess)
        self.report("test_check_guess_all_incorrect", result == (0, 0))

    def test_check_guess_partial_overlap(self):
        secret_code = [0, 1, 2, 3]
        guess = [1, 0, 3, 2]
        result = check_guess(secret_code, guess)
        self.report("test_check_guess_partial_overlap", result == (0, 4))

    def test_cleanup_input_mixed_characters(self):
        result = cleanup_input("a1b2c3d4")
        self.report("test_cleanup_input_mixed_characters", result == [1, 2, 3, 4])

    def test_cleanup_input_empty_string(self):
        result = cleanup_input("")
        self.report("test_cleanup_input_empty_string", result == [])

    def test_mastermind_bot_minimal_range(self):
        bot = MastermindBot(1, 2)
        bot.filter_possible_guesses([0], (1, 0))
        self.report("test_mastermind_bot_minimal_range", len(bot.possible_codes) == 1)

    def test_mastermind_bot_max_range(self):
        bot = MastermindBot(7, 8)
        bot.filter_possible_guesses([0], (1, 0))
        self.report("test_mastermind_bot_max_range", len(bot.possible_codes) > 0)

    @patch("requests.get")
    def test_generate_secret_code_api_fallback(self, mock_get):
        mock_get.side_effect = Exception("API failure")
        secret_code = generate_secret_code(4, 8)
        passed = len(secret_code) == 4 and all(0 <= digit < 8 for digit in secret_code)
        self.report("test_generate_secret_code_api_fallback", passed)


if __name__ == "__main__":
    unittest.main()
