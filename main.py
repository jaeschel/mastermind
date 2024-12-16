from game_settings import GameSettings
from mastermindbot import MastermindBot
from game_logic import generate_secret_code, check_guess
from tools import display_guess_history, get_user_guess


def play_game():
    """
    Main game for Mastermind
    """
    attempts = 10
    history = []
    hint_used = False

    settings = GameSettings()
    code_length, digit_range = settings.configure()
    hintbot = MastermindBot(code_length, digit_range)
    secret_code = generate_secret_code(code_length, digit_range)

    while attempts > 0:

        print("\nNumber of attempts left : ", attempts)
        guess = get_user_guess(hint_used, code_length, digit_range)

        if str(guess).lower().strip() == 'hint':
            if history:  # if they've played a game
                if hint_used == False:
                    hint = hintbot.get_hint(history)
                    print('My best guess is: ', hint)
                    hint_used = True
                else:
                    print('My best guess is: ', hint)
                continue
            else:
                print('\nYou have to play 1 game first before you can hint!')
                continue

        try:
            if guess:
                correct_pos, correct_num = check_guess(secret_code, guess)
                history.append((guess, (correct_pos, correct_num)))
                attempts -= 1
                hint_used = False
                print('\n')
                display_guess_history(history)
    
            if correct_pos == code_length:
                print(f"\nYou've Guessed the Code Correctly!\nThe Solved Code was : {secret_code}")
                break

        except Exception as e:
            print("\nUnexpected Error:", e)
            continue  # restart loop
    if attempts == 0:
        print(f"\nSorry! You've run out of attempts\nThe Correct Code was : {secret_code}")


def main():
    while True:
        play_game()
        if input("\nPlay Again? Type 'yes' or Any Other Key to Exit : ").lower().strip() != "yes":
            print("\nThanks for Playing! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
