import random
import requests


def generate_secret_code(code_length, digit_range):
    """
    Generates the secret code from a specified length and digit range

        Args:
            code_length(int) = length of code
            digit_range(int) = range of digits to choose from

        Returns:
            List[int] = a list of integers that represents the secret code
                Example: [1,2,3,4]
    """
    url = "https://www.random.org/integers"
    params = {
        'num': code_length,
        'min': 0,
        'max': digit_range-1,
        'col': 1,
        'base': 10,
        'format': 'plain',
        'rnd': 'new'
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            secret_code = list(map(int, response.text.strip().splitlines()))
            return secret_code

    except Exception as e:
        print("hmm... it didn't work. ERROR: ", e)
        print("Random.org API failed. Grabbing the code locally...")
        secret_code = [random.randint(0, digit_range - 1) for _ in range(code_length)]
        return secret_code


def check_guess(secret_code, guess):
    """
    Evaluates the positons of guess to the secret code

        Args:
            secrete_code(list[int]) = target code
            guess(list[int]) = the user's guess
        Returns:
            tuple(int,int) = number of correct positions and correct digits
    """
    # zip() = pairs each element
    correct_position = sum(a == b for a, b in list(zip(secret_code, guess)))  # if so returns number of True

    # for each individual number in guess, compare to its frequency in secret_code and guess
    # return the smaller number, then add them together
    correct_num = sum(min(secret_code.count(n), guess.count(n)) for n in set(guess))
    correct_num = correct_num - correct_position

    return(correct_position, correct_num)


def prompt_play_again():
    """
    Prompts the user to play again.
    """
    while True:
        response = input("\nDo you want to play again? (yes/no) : ").lower().strip()
        if response == "yes":
            from main import mastermind
            mastermind()
            break
        elif response == "no":
            print("\nThanks for Playing! Goodbye!\n")
            break
        else:
            print("\nInvalid input. Please enter either 'yes' or 'no'")
