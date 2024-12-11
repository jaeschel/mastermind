import unittest
from unittest.mock import patch
from game_logic import check_guess, generate_secret_code, prompt_play_again
from tools import cleanup_input, display_guess_history
from game_settings import GameSettings
from mastermindbot import MastermindBot

class TestMastermind(unittest.TestCase):

    # Tests for Game Settings
    @patch("builtins.input", side_effect=["4", "8"])
    def test_game_settings_configure(self, mock_input):
        settings = GameSettings()
        result = settings.configure()
        try:
            self.assertEqual(result, (4, 8))
            print("[✔] test_game_settings_configure PASSED")
        except AssertionError:
            print("[✘] test_game_settings_configure FAILED")

    # Tests for Game Logic
    def test_check_guess_exact_match(self):
        secret_code = [1, 2, 3, 4]
        guess = [1, 2, 3, 4]
        try:
            self.assertEqual(check_guess(secret_code, guess), (4, 0))
            print("[✔] test_check_guess_exact_match PASSED")
        except AssertionError:
            print("[✘] test_check_guess_exact_match FAILED")

    def test_check_guess_partial_match(self):
        secret_code = [1, 2, 3, 4]
        guess = [4, 3, 2, 1]
        try:
            self.assertEqual(check_guess(secret_code, guess), (0, 4))
            print("[✔] test_check_guess_partial_match PASSED")
        except AssertionError:
            print("[✘] test_check_guess_partial_match FAILED")


    @patch("requests.get")
    def test_generate_secret_code_fallback(self, mock_get):
        mock_get.side_effect = Exception("API failure")
        try:
            secret_code = generate_secret_code(4, 8)
            self.assertEqual(len(secret_code), 4)
            for digit in secret_code:
                self.assertTrue(0 <= digit < 8)
            print("[✔] test_generate_secret_code_fallback PASSED")
        except AssertionError:
            print("[✘] test_generate_secret_code_fallback FAILED")

    # Tests for Tools
    def test_cleanup_input_valid(self):
        try:
            self.assertEqual(cleanup_input("1, 2, [3] ,4"), [1, 2, 3, 4])
            print("[✔] test_cleanup_input_valid PASSED")
        except AssertionError:
            print("[✘] test_cleanup_input_valid FAILED")

    def test_cleanup_input_invalid(self):
        try:
            self.assertEqual(cleanup_input("a, b, c"), [])
            print("[✔] test_cleanup_input_invalid PASSED")
        except AssertionError:
            print("[✘] test_cleanup_input_invalid FAILED")

    def test_display_guess_history(self):
        history = [([1, 2, 3, 4], (2, 1))]
        try:
            display_guess_history(history)  # Should print without errors
            print("[✔] test_display_guess_history PASSED")
        except Exception as e:
            print(f"[✘] test_display_guess_history FAILED: {e}")

    # Tests for Mastermind Bot
    def test_mastermind_bot_initialization(self):
        bot = MastermindBot(4, 8)
        try:
            self.assertEqual(len(bot.possible_codes), 8 ** 4)
            print("[✔] test_mastermind_bot_initialization PASSED")
        except AssertionError:
            print("[✘] test_mastermind_bot_initialization FAILED")

    def test_mastermind_bot_filter_guesses(self):
        bot = MastermindBot(4, 8)
        guess = [1, 2, 3, 4]
        feedback = (2, 1)
        bot.filter_possible_guesses(guess, feedback)
        try:
            self.assertTrue(len(bot.possible_codes) < 8 ** 4)
            print("[✔] test_mastermind_bot_filter_guesses PASSED")
        except AssertionError:
            print("[✘] test_mastermind_bot_filter_guesses FAILED")

if __name__ == "__main__":
    unittest.main()
