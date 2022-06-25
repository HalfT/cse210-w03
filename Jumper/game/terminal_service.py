class TerminalService:

    """ Handles the visual and output of the parachute visuals and guesses

        Attributes:
            parachute (list): visual for the parachute

    """

    def __init__(self):

        """parachute visuals put in a list
        
        Args:
            self (TerminalService): An instance of TerminalService.

        """

        self.parachute = [
"""
  ___
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
  _ _
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
     
 /___\\
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
  ___
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
  _ _ 
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
 \\   /
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
  \\ /
   O
  /|\\
  / \\
^^^^^^^
""",
"""
   X
  /|\\
  / \\
^^^^^^^
"""]

    def display_parachute(self, parachute):

        """ displayes parachute

        Args:
            self (TerminalService): An instance of TerminalService.
            integer (integer): for the list to push out the correct parachute visual

        
        """
        
        print(self.parachute[parachute])
        

    def question(self,guess):

        """ displayes the question to the user

        Args:
            self (TerminalService): An instance of TerminalService.
            string (string): A string to print to the terminal.
        
        """
        return input(guess)