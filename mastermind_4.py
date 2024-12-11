import requests
import random
from itertools import product

# 1. Generate the Code
def generate_code(length,option):
    url = "https://www.random.org/integers"
    params = {
        'num' : length,
        'min' : 0,
        'max' : option-1,
        'col' : 1,
        'base' : 10,
        'format' : 'plain',
        'rnd' : 'new'
    }

    try:
        response = requests.get(url, params= params)
        if response.status_code == 200:
            secret_code = list(map(int, response.text.strip().splitlines()))
            #print(secret_code)
            return secret_code
        
        else:
            print ("hmm... the API request failed")
            print ("generating secret code locally...")
            secret_code = [random.randint(0, option-1) for _ in range(length)]
            #print (secret_code)
            return secret_code
        print ("\nlet's start!")

    except Exception as e:
       print ("hmm... it didn't work. ERROR: ", e)
       print ("Random.org API failed. Grabbing the code locally...")
       secret_code = [random.randint(0, option -1) for _ in range(length)]
       print ("\nlet's start!")
       #print(secret_code)
       return secret_code
    
#1a. Clean Up Guess to allow spaces, commas and/or none
def cleanup(guess):
    try:
        #cleaned_guess = list(map(int, guess.replace(',',' ').replace(' ', '').strip()))
        #print(cleaned_guess)
        cleaned_guess = guess.replace(',',' ').replace(' ', '').replace('[', '').replace(']', '').strip()
        #print(cleaned_guess)
        for digit in cleaned_guess:
            if not digit.isdigit():
                break # leave the for loop
            cleaned_guess = list(map(int,cleaned_guess))
            return cleaned_guess
    except ValueError:
        # print(f"\nInvalid input. Please enter {length} numbers between 0 and 7.")
        return []

#2. Check Guesses and print answer
def check_guess(secret_code, guess):
    #zip() = pairs each element and checks to see if they're the same. If so it returns True. If not it returns False
    correct_position = sum([a == b for a, b in list(zip(secret_code, guess))])

    # for each individual number in guess, compare to it's frequency in secret_code and guess
    # return the smaller number, then add them together
    correct_num = sum(min(secret_code.count(n), guess.count(n)) for n in set(guess))
    correct_num = correct_num - correct_position

    # print("correct_pos : ", correct_position)
    # print("correct_num : ", correct_num)
    return(correct_position, correct_num)

#3. Keep Track of History
def guess_history(history):
    print("Guess History")
    for i, j in enumerate(history, 1):
        guessed_code, (correct_pos, correct_num) = j
        print (f"\nGuessed Code #{i} :  {guessed_code}")
        print (f"   Right Positions: {correct_pos}")
        print (f"   Right Number, Wrong positions: {correct_num}")

#4. Play Again
def play_again():
    while True:
        response = input("\nDo you want to play again? (yes/no) : ").lower().strip()
        if response == "yes":
            mastermind()
            break
        elif response == "no":
            print("\nThanks for Playing! Goodbye!\n")
            break
        else:
            print("\nInvalid input. Please enter either 'yes' or 'no'")

class MastermindBot:
    def __init__(self, length, option):
        self.possible_codes = list(product(range(option), repeat=length))

    def delete_impossible(self, guess, feedback):
        self.possible_codes = [
            code for code in self.possible_codes
            if check_guess(code,guess) == feedback
        ]

    def make_guess(self,history):
        for guess,feedback in history:
            self.delete_impossible(guess,feedback)

        if not self.possible_codes:
            return None
        #print(len(self.possible_codes))
        return random.choice(self.possible_codes)
        

class GameModes():
    def __init__(self):
        self.length = None
        self.option = None

    def set(self):
        while True:
            self.length = input('\nHow many digits do you want to solve for? : ').strip()
            self.length = int(self.length)
            try:
                if 1 <= self.length <= 9:
                    break
                else:
                    print('\nPlease enter a number between 1 and 9!')
            except ValueError:
                print("\nInvalid input! Enter a positive integer!")

        while True:
            try:
                self.option = input('\nHow many numbers to choose from? : ').strip()
                self.option = int(self.option)
                if 1 <= self.option <=8 :
                    break
                else:
                    print('\nPlease enter a number between 1 and 8!')

            except ValueError:
                print("\nInvalid input! Enter a positive integer!")
        
        return self.length, self.option
        
# def testGameMode():
#     gm = GameModes()
#     length = gm.set()
#     return length

#5. Gameplay
def mastermind():
    attempts = 10
    history = []
    hint_used = False
    
    gm = GameModes()
    length, option = gm.set()
    print(length)
    print(option)
    hintbot = MastermindBot(length,option)
    secret_code = generate_code(length,option)
    print(secret_code)
    
    while attempts > 0:
        print("\nNumber of attempts left : ", attempts)
        if hint_used == True:
            guess = input(f"\nEnter your {length}-number guess : ")
        else:
            guess = input(f"\nEnter your {length}-number guess, or type 'hint' for a HINT!: ")

        if guess.lower().strip() == 'hint':
            if history: #if they've played a game
                if hint_used == False:
                    hint = hintbot.make_guess(history)
                    print('My best guess is: ', hint)
                    hint_used = True
                else:
                    print("\nYou've already used a hint this round!")
                    print('My best guess is: ', hint)
                continue
            else:
                print('You have to play 1 game first before you can HINT!')
                continue

        #check if integer before we run clean up
        # if not isinstance(guess.lower().strip(), int):
        #     print(f"\nInvalid input. Enter exactly {length} numbers between 0 and 7.")
        #     continue

        guess = cleanup(guess)

        try:
            if not guess or len(guess) != length or any(n < 0 or n >= option for n in set(guess)):
                print(f"\nInvalid input. Enter exactly {length} numbers between 0 and {option}.")
                continue # restart the loop
            elif not guess:
                print(f"\nInvalid input. Enter exactly {length} numbers between 0 and {option}.")
                continue # restart the loop
            else:
                correct_pos, correct_num = check_guess(secret_code, guess)
                history.append((guess, (correct_pos, correct_num)))
                attempts -= 1
                hint_used = False

                if (correct_pos == length):
                    print (f"\nYou've Guessed the Code Correctly!\nThe Solved Code is : {secret_code}")
                    play_again()
                    break
                else:
                    print('\n')
                    guess_history(history)

        except Exception as e:
            print ("\nUnexpected Error:", e)
            continue #restart loop
    if attempts == 0:
        print(f"\nSorry! You've run out of attempts\nThe Correct Code is : {secret_code}")
        play_again()
    
#Run it
mastermind()