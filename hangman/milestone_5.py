import random

# Created a list of words to be used in the game


class Hangman:
    def __init__(self, word_list,num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = "_" * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            print(f"'{guess}' is not in the word. Try again!")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
           

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                
                if self.num_letters == 0:
                    print(f"Congratulations! You guessed the word: '{self.word}'.")
                    break
                if self.num_lives == 0:
                    print(f"Game over! The word was: '{self.word}'.")
                    break
            


def play_game(word_list):
    game = Hangman(word_list)
    game.ask_for_input()

word = ['apple', 'banana', 'orange', 'pear','pineapple']    
play_game(word)