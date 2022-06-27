from word import Word
from hangman import Hangman
import os

class Game:

    MAXLIVES = 7

    # Initializes the game
    def __init__(self, fileName):
        self.fileName = fileName
        self.word = Word(self.fileName)
        self.guesses = []
        self.wrong_guesses = []


    # Returns the introduction to the game
    def get_introduction(self):
        introduction_string = [
            "Welcome to Hangman!",
            "Your goal is to guess the word by guessing individual letters.",
            f"You have {Game.MAXLIVES} tries.",
        ]
        return '\n'.join(introduction_string)

    
    # Asks the user for a guess and returns the guess
    def ask_user_guess(self):
        guess = input("Guess a letter (a-z): ")

        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            return self.ask_user_guess()
        
        if len(guess) > 1:
            print("Please enter only one letter.")
            return self.ask_user_guess()
        
        if (guess.lower() in self.guesses) or (guess.lower() in self.wrong_guesses):
            print("You already guessed that letter.")
            return self.ask_user_guess()

        return guess.lower()
        
    
    # Checks if the guess is correct and returns True or False
    def check_guess(self, guess):
        return guess in self.word.get_word()


    # Clears the screen
    def clear_screen(self):
        return os.system('cls' if os.name == 'nt' else 'clear')


    # The main game loop, which runs until the user either wins or loses
    def start(self):
        # Introduction
        self.clear_screen()
        print(self.get_introduction())
        print(self.word.get_word_dashed(self.guesses))
        
        # Main game loop
        guess = self.ask_user_guess()
        while len(self.wrong_guesses) <= Game.MAXLIVES:
            self.clearScreen()

            # Check if the guess is correct
            if self.check_guess(guess):
                print("Good guess!")
                self.guesses.append(guess)
            else:
                print("Wrong guess!")
                self.wrong_guesses.append(guess)
            
            # Check if the user has won
            if "_" not in self.word.get_word_dashed(self.guesses):
                print(f"Congratulations! You guessed the word {self.word.get_word()}!")
                break

            # Check if the user lost
            if len(self.wrong_guesses) > Game.MAXLIVES:
                print(f"You lost! The word was {self.word.get_word()}.")
                break
            
            # Print the current state of the game
            print(self.word.get_word_dashed(self.guesses))
            print(Hangman.get_cuttent_state(self.wrong_guesses))
            print(f"Wrong guesses: {', '.join(self.wrong_guesses)}")

            guess = self.ask_user_guess()