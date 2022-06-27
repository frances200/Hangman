class Hangman:

    # The states of the game *must be 1 higher than the number of lives*
    STATES = ['''
    +---+
        |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
        |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
========='''
    ]


    # Get the current state of the game depending on the amount of wrong guesses
    def get_current_state(wrong_guesses) -> str:
        return Hangman.STATES[len(wrong_guesses)]