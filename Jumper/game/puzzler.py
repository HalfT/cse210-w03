import random

class Puzzler:

    """Builds the hidden word with random a random chance for the word.

    Attributes:
            _word (list): selects a word for the game

    
    """

    def __init__(self):

        """Construcs a puzzle.
        
        Args:
            self (Puzzler): An instance of Puzzler.
            word (string): Word for the game.
        """

        self._words = ["jumbo", "eagle", "break", "earth", "lucky"]
        self._word = ""

    def choose_word(self):

        """ Pics random number to select a random word.
            returns _word
            
            Args:
                self (Puzzler): An instance of Puzzler.
                word (string): Word for the game.
        """

        self._word = self._words[random.randint(1,5) - 1 ]

        


    