import random

class Word:

    # Initializes the word
    def __init__(self, fileName):
        self.word = self.randomize(fileName)

    
    # Returns a random word from a wordlist
    def randomize(self, fileName):
        with open(fileName, 'r') as wordlist:
            words = wordlist.readlines()
            word = random.choice(words).strip()
        return word
    

    # Returns the word
    def get_word(self):
        return self.word
    

    # Returns the current state of the word as a string
    def get_word_dashed(self, guesses):
        word = []
        for letter in self.word:
            if letter in guesses:
                word.append(letter)
                continue
            word.append('_')
        return ''.join(word)