import unittest
from unittest.mock import patch, MagicMock
from game_logic import check_guess, generate_secret_code
from tools import cleanup_guess, validate_input, display_guess_history
from game_settings import GameSettings
from mastermindbot import MastermindBot

class TestMastermindGame(unittest.TestCase):

    def test_check_guess_correct_positions(self):
        secret_code = [1, 2, 3, 4]
        guess = [1, 2, 3, 4]
        result = check_guess(secret_code, guess)
        self.assertEqual(result, (4, 0))

    def test_check_guess_partial_match(self):
        secret_code = [1, 2, 3, 4]
        guess = [4, 3, 2, 1]
        result = check_guess(secret_code, guess)
        self.assertEqual(result, (0, 4))

    def test_check_guess_mixed_match(self):
        secret_code = [1, 2, 3, 4]
        guess = [1, 3, 2, 5]
        result = check_guess(secret_code, guess)
        self.assertEqual(result, (1, 2))

    @patch("requests.get")
    def test_generate_secret_code_api_success(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, text="1\n2\n3\n4\n")
        result = generate_secret_code(4, 8)
        self.assertEqual(result, [1, 2, 3, 4])

    @patch("requests.get", side_effect=Exception("API failure"))
    def test_generate_secret_code_api_failure(self, mock_get):
        result = generate_secret_code(4, 8)
        self.assertEqual(len(result), 4)
        self.assertTrue(all(0 <= num < 8 for num in result))

    def test_cleanup_guess_valid_input(self):
        guess = "1 2 3 4"
        result = cleanup_guess(guess)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_cleanup_guess_invalid_input(self):
        guess = "a b c d"
        result = cleanup_guess(guess)
        self.assertEqual(result, [])

    def test_validate_input_correct(self):
        guess = [1, 2, 3, 4]
        result = validate_input(guess, 4, 8)
        self.assertEqual(result, guess)

    def test_validate_input_incorrect_length(self):
        guess = [1, 2, 3]
        result = validate_input(guess, 4, 8)
        self.assertEqual(result, [])

    def test_game_settings_valid_input(self):
        with patch("builtins.input", side_effect=["4", "8"]):
            settings = GameSettings()
            result = settings.configure()
            self.assertEqual(result, (4, 8))

    def test_mastermind_bot_hint(self):
        bot = MastermindBot(4, 8)
        history = [([1, 2, 3, 4], (2, 2))]
        hint = bot.get_hint(history)
        self.assertEqual(len(hint), 4)

    def test_display_guess_history(self):
        history = [([1, 2, 3, 4], (2, 2)), ([5, 6, 7, 8], (0, 0))]
        with patch("builtins.print") as mock_print:
            display_guess_history(history)
            mock_print.assert_any_call("Guessed Code #1 :  [1, 2, 3, 4]")
            mock_print.assert_any_call("Guessed Code #2 :  [5, 6, 7, 8]")

if __name__ == "__main__":
    unittest.main()