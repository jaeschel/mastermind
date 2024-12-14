class GameSettings():
    """
    Allows the user to configure their own settings
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
            self.code_length = input('\nHow many digits do you want to solve for? : ').strip()
            try:
                if 1 <= int(self.code_length) <= 7:
                    break
                else:
                    print('\nEnter code length (1-7!')
            except ValueError:
                print("\nInvalid input! Enter a positive integer!")

        while True:
            try:
                self.digit_range = input('\nEnter digit range (2-8): ').strip()
                if 2 <= int(self.digit_range) <= 8:
                    break
                else:
                    print('\nPlease enter a number between 2 and 8!')

            except ValueError:
                print("\nInvalid input! Enter a positive integer!")

        return int(self.code_length), int(self.digit_range)
