import random

class Hangman:
    def __init__(self, words, max_attempts=6):
        self.words = words
        self.max_attempts = max_attempts
        self.attempts = 0
        self.current_word = random.choice(self.words)
        self.guessed_letters = set()
        self.display_word = ['_'] * len(self.current_word)

    def display_current_state(self):
        print("Current word: ", " ".join(self.display_word))
        print("Guessed letters: ", " ".join(sorted(self.guessed_letters)))
        print(f"Attempts left: {self.max_attempts - self.attempts}")

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            self.attempts += 1           
            return
        
        self.guessed_letters.add(letter)
        if letter in self.current_word:
            print("Correct guess!")
            for i, char in enumerate(self.current_word):
                if char == letter:
                    self.display_word[i] = letter
        else:
            print("Incorrect guess!")
            self.attempts += 1

    def is_game_over(self):
        return self.attempts >= self.max_attempts or '_' not in self.display_word

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            self.display_current_state()
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            self.guess_letter(guess)
        
        if '_' not in self.display_word:
            print("Congratulations! You've guessed the word:", self.current_word)
        else:
            print("Sorry, you ran out of attempts. The word was:", self.current_word)

# List of words to choose from
words_list = ["across","carrier","capable","chain","activist","chemical","classroom","coffee"]
# Create a Hangman instance and start the game
hangman_game = Hangman(words_list)
hangman_game.play()
