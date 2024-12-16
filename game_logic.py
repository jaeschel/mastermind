import random
import requests


def generate_secret_code(code_length, digit_range):
    """
    Generates the secret code from a specified length and digit range

        Args:
            code_length(int) = Length of code between 1-7.
            digit_range(int) = Range of digits to choose from between 2-8.

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
    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        try:
            response = requests.get(url, params=params, timeout=5)
            if response.status_code == 200:
                secret_code = list(map(int, response.text.strip().splitlines()))
                return secret_code

        except Exception as e:
            print("API Call ERROR: ", e)
            retry_count += 1
        
    print("Random.org API failed. Grabbing the code locally...")
    secret_code = [random.randint(0, digit_range - 1) for _ in range(code_length)]
    return secret_code


def check_guess(secret_code, guess):
    """
    Evaluates the positons of guess to the secret code

        Args:
            secrete_code(list[int]) = target code.
            guess(list[int]) = the user's guess.
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

