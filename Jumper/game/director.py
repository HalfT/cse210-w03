from game.guesser import Guesser
from game.puzzler import Puzzler
from game.terminal_service import TerminalService

class Director:
    """ Starts the game and follows commands.

    Atributes:
        is_playing (boolean): Check to see if still playing
        guesser (Guesser): The game's way to process data
        puzzler (Puzzler): Chooses a random word for the game
        terminal_service: helps print out visuals.
    
    """

    def __init__(self):

        """ Buids a new Director.

        Args:
            self (Director): An instance of Director.
        
        """

        self._is_playing = True
        self._guesser = Guesser()
        self._puzzler = Puzzler()
        self._terminal_service = TerminalService()
        


    def start_game(self):

        """ Starts the Game then begins a loop for continue guesses.

        Args:
            self (Director): An instance of Director.
        
        """
        
        print ("\nLets play Jumper! (hangman)")
        self._puzzler.choose_word()

        self._do_outputs()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):

        """ Gets input from the user on the guess of the letter in the word

        Args:
            self (Director): An instance of Director.
        
        """

        self.guess = self._terminal_service.question("Please guess a letter [a-z]: ")
        print()

    def _do_updates(self):

        """ compares and updates the guess to the random word.
            updates tries

        Args:
            self (Director): An instance of Director.
        
        """

        word = self._puzzler._word
        self._guesser.check_guess(self.guess, word)
        self._is_playing = self._guesser._update_status(word)

    def _do_outputs(self):
 
        """ Prints the current status of the game

        Args:
            self (Director): An instance of Director.
        
        """

        self._guesser._status()

