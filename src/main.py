from game import Game

# Start of the program, creates a new game
if __name__ == '__main__':
    userInput = "y"
    while userInput.lower() == "y":
        game = Game("assets\\wordlist.txt")
        game.start()
        userInput = input("Would you like to play again? (y/n) ")