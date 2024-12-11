class GameSettings():
    """
    Allows the user to congfigure their own settings
    """
    def __init__(self):
        self.code_length = None
        self.digit_range = None

    def configure(self):
        """
        Prompting user for code length and digit range

            Returns:
                tuple[int,int]: a tuple of two positive integers [code_length,digit_range]
        
        """
        while True:
            self.code_length = int(input('\nHow many digits do you want to solve for? : ').strip())
            try:
                if 1 <= self.code_length <= 9:
                    break
                else:
                    print('\nEnter code length (1-9!')
            except ValueError:
                print("\nInvalid input! Enter a positive integer!")

        while True:
            try:
                self.digit_range = int(input('\nEnter digit range (2-8): ').strip())
                if 2 <= self.digit_range <=8 :
                    break
                else:
                    print('\nPlease enter a number between 2 and 8!')

            except ValueError:
                print("\nInvalid input! Enter a positive integer!")
        
        return self.code_length, self.digit_range