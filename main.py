from game_settings import GameSettings
from mastermindbot import MastermindBot
from game_logic import generate_secret_code, check_guess, prompt_play_again
from tools import cleanup_input, display_guess_history

def mastermind():
    """
    Main game for Mastermind
    """
    attempts = 10
    history = []
    hint_used = False
    
    settings = GameSettings()
    code_length, digit_range = settings.configure()
    hintbot = MastermindBot(code_length,digit_range)
    secret_code = generate_secret_code(code_length,digit_range)
    
    while attempts > 0:
        print("\nNumber of attempts left : ", attempts)
        if hint_used == True:
            guess = input(f"\nEnter your {code_length}-number guess : ")
        else:
            guess = input(f"\nEnter your {code_length}-number guess, or type 'hint' for a HINT!: ")

        if guess.lower().strip() == 'hint':
            if history: #if they've played a game
                if hint_used == False:
                    hint = hintbot.get_hint(history)
                    print('My best guess is: ', hint)
                    hint_used = True
                else:
                    print("\nYou've already used a hint this round!")
                    print('My best guess is: ', hint)
                continue
            else:
                print('\nYou have to play 1 game first before you can HINT!')
                continue

        guess = cleanup_input(guess)

        try:
            if not guess or len(guess) != code_length or any(n < 0 or n >= digit_range for n in set(guess)):
                print(f"\nInvalid input. Enter exactly {code_length} numbers between 0 and {digit_range-1}.")
                continue # restart the loop
            elif not guess:
                print(f"\nInvalid input. Enter exactly {code_length} numbers between 0 and {digit_range-1}.")
                continue # restart the loop
            else:
                correct_pos, correct_num = check_guess(secret_code, guess)
                history.append((guess, (correct_pos, correct_num)))
                attempts -= 1
                hint_used = False

                if (correct_pos == code_length):
                    print (f"\nYou've Guessed the Code Correctly!\nThe Solved Code is : {secret_code}")
                    prompt_play_again()
                    break
                else:
                    print('\n')
                    display_guess_history(history)

        except Exception as e:
            print ("\nUnexpected Error:", e)
            continue #restart loop
    if attempts == 0:
        print(f"\nSorry! You've run out of attempts\nThe Correct Code is : {secret_code}")
        prompt_play_again()
    
if __name__ == "__main__":
    mastermind()