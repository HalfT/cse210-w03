from game.terminal_service import TerminalService

class Guesser:

    """Keeps track of the guess and the chosen word for the game.

    Attributes:
            terminal_service: helps print out visuals.
            word_complection (list): keeps track of current progress of guesses.
            tries (integer): keeps track of the tries for end of game and to display parachute
            _correct_guess (list): keeps track of the correct guess to build wor_completion as game goes on

    
    """

    def __init__(self):

        """ Contructs a new guesser.

        Args:
            self (Guesser): An instance of Guesser.
        
        """
        
        self._terminal_service = TerminalService()
        self.word_completion = " _ " * 5
        self.tries = 0
        self._correct_guess = [""]

    def _status(self):

        """ Prints status of game.

        Args:
            self (Guesser): An instance of Guesser.
        
        """

        print()
        print (self.word_completion)
        self._terminal_service.display_parachute(self.tries)
        self.tries += 1
        

    def check_guess(self, guess, word):

        """ Compares guess to the chosen word for the game. 
            prints if guess is correct or not
            helps with current guess count

        Args:
            self (Guesser): An instance of Guesser.
            guess (string): input from the user.
            word (string): the chosen word for the game.
        
        """
        
        
        if guess not in word:
            print (f"{guess} is not in the word.")

        else:
            print (f"Good Job, {guess} is in the word!")
            self._correct_guess.append(guess)

            build_word = []
            for i in word:
                if i in self._correct_guess:
                    build_word.append(i)
                else:
                    build_word.append("_ ")
            
            self.word_completion = "".join(build_word)
            self.tries -= 1

    def _update_status(self, word):

        """ Check to see if the game will continue or not

        Args:
            self (Guesser): An instance of Guesser.
            word (string): help to see if the word and word_completion is the same

        Returns:
            boolean: To continue game or not.
        
        """

        if self.tries == 7:
            print("\nSorry you are out of guesses. Better luck next time.\n")
            return False
        
        elif self.word_completion == word:
            print(f"\nCongatulations! You guessed the word!")
            return False

        else:
            return True



                


    
