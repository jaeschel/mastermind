import requests
import random

# 1. Generate the Code
def generate_code():
    url = "https://www.random.org/integers"
    params = {
        'num' : 4,
        'min' : 0,
        'max' : 7,
        'col' : 1,
        'base' : 10,
        'format' : 'plain',
        'rnd' : 'new'
    }

    try:
        response = requests.get(url, params= params)
        if response.status_code == 200:
            secret_code = list(map(int, response.text.strip().splitlines()))
            print ("\nlet's start!")
            #print(secret_code)
            return secret_code
        
        else:
            print ("hmm... the API request failed")
            print ("generating secret code locally...")
            secret_code = [random.randint(0, 7) for _ in range(4)]
            print ("\nlet's start!")
            #print (secret_code)
            return secret_code
        
    except Exception as e:
       print ("hmm... it didn't work. ERROR: ", e)
       print ("generating secret code locally...")
       secret_code = [random.randint(0, 7) for _ in range(4)]
       print ("\nlet's start!")
       #print(secret_code)
       return secret_code
    
#1a. Clean Up Guess to allow spaces, commas and/or none
def cleanup(guess):
    try:
        cleaned_guess = list(map(int, guess.replace(',',' ').replace(' ', '').strip()))
        #print(cleaned_guess)
        return cleaned_guess

    except ValueError:
        print("Invalid input. Please enter four numbers between 0 and 7.")
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
            print("\nThanks for Playing! Goodbye!")
            break
        else:
            print("\nInvalid input. Please enter either 'yes' or 'no'")
            continue

class MastermindAI:
    def __init__(self):
        self.possible_codes = [
            [a,b,c,d]
            for a in range(8)
            for b in range(8)
            for c in range(8)
            for d in range(8)
        ]

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
        print(len(self.possible_codes))
        return random.choice(self.possible_codes)
        

#5. Gameplay
def mastermind():
    attempts = 10
    secret_code = generate_code()
    #print(secret_code)
    history = []
    ai = MastermindAI()

    while attempts > 0:
        print("\nNumber of attempts left : ", attempts)
        guess = input("\nEnter your 4-number guess, or type 'hint' for a HINT!: ")
        if guess.lower().strip() == 'hint':
            if history: #if they've played a game
                hint = ai.make_guess(history)
                print('My best guess is: ', hint)
                continue
            else:
                print('You have to play 1 game first before you can HINT!')
                continue
        guess = cleanup(guess)
        try:
            if len(guess) != 4 or any(n < 0 or n > 7 for n in set(guess)):
                print("\nInvalid input. Enter exactly FOUR numbers between 0 and 7.")
                continue # restart the loop
            else:
                correct_pos, correct_num = check_guess(secret_code, guess)
                history.append((guess, (correct_pos, correct_num)))
                attempts -= 1

                if (correct_pos == 4):
                    print (f"\nYou've Guessed the Code Correctly!\nThe Solved Code is : {secret_code}")
                    play_again()
                    break
                else:
                    print('\n')
                    guess_history(history)

        except Exception as e:
            print ("hmm... Error", e)
            continue #restart loop
    if attempts == 0:
        print(f"\nSorry! You've run out of attempts\nthe Correct Code is : {secret_code}")
        play_again()
        exit()
    
#Run it
mastermind()