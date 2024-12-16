import random

class GameSettings():
    """
    Allows the user to configure their own settings
    """
    def __init__(self):
        self.code_length = None
        self.digit_range = None
        self.digit_range_min = None
        self.digit_range_max = None
        self.MAX_CODE_LENGTH = 7
        self.MIN_CODE_LENGTH = 1
        self.MAX_DIGIT_RANGE = 9
        self.MIN_DIGIT_RANGE = 2

# prompt the user for the min and max values
# generate a random number between min and max
# correct prompts

    def configure(self):
        """
        Prompting user for code length and digit range

            Returns:
                tuple[int,int]: a tuple of two positive integers [code_length,digit_range]
        """
        while True:
            # self.start_value = random.randint(0,9)
            # print("start" , self.start_value)
            self.code_length = input(f'\nEnter code length btwn {self.MIN_CODE_LENGTH} - {self.MAX_CODE_LENGTH}! : ').strip()
            try:
                if self.MIN_CODE_LENGTH <= int(self.code_length) <= self.MAX_CODE_LENGTH:
                    break
                else:
                    print(f'\nInvalid input! Number not within bounds.')
                    
            except ValueError as e:
                print(f"\nInvalid input! {e}")

        while True:
            try:
                
                self.digit_range_min = input(f'\nEnter digit min ({self.MIN_DIGIT_RANGE}-{self.MAX_DIGIT_RANGE}) : ').strip()
                self.digit_range_max = input(f'\nEnter digit max ({self.MIN_DIGIT_RANGE}-{self.MAX_DIGIT_RANGE}) : ').strip()
                
                self.digit_range = int(self.digit_range_max) - int(self.digit_range_min)

                if self.MIN_DIGIT_RANGE <= int(self.digit_range) <= self.MAX_DIGIT_RANGE:
                    break
                else:
                    print(f'\nInvalid input! Number not within bounds.')

            except ValueError:
                print(f"\nInvalid input! {e}")

        return int(self.code_length), int(self.digit_range), int(self.digit_range_min), int(self.digit_range_max)
