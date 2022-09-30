import random #random for choosing random words out of a list
import string
class Hangman:

    def __init__(self, word_list, num_lives):
        pass
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        HANGMAN6 = "+---+ \n  O  \n /|\ \n / \ \n ==="
        
        print(f"The mystery word has {len(self.word)} characters")
        print(HANGMAN6)
        print(self.word_guessed)
        
    #creating method for checking letter
    def check_guess(self, guess):
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, element in enumerate(self.word): 
                if guess == element:
                    self.word_guessed[index] = element
            print(self.word_guessed)
            self.num_letters -=1
            self.print_hangman()
            
        else:
            self.num_lives -=1
            self.print_hangman()
            print(f"Sorry, {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} tries left")

        self.list_of_guesses.append(guess)

    #method for input
    def ask_for_input(self):
        pass
        alphabets = set(string.ascii_lowercase) #making a set of lower case alphabets for the elif statements
        while True:
            guess = input("Please enter a character: ")
            guess = guess.lower() #converting into lowercase letters to compare to s
            if len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess not in alphabets:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                print(f"The letters that you've tried are {self.list_of_guesses}")
            else:
                print(f"Your guess is {guess} ")
                #self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
    
    #ask_for_input()
    def print_hangman(self):

        HANGMAN6 = "+---+ \n  O  \n /|\ \n / \ \n ===" #using capital letters to indicate that variable will stay constant
        HANGMAN5 = "+---+ \n  O  \n /|\ \n /   \n ==="
        HANGMAN4 = "+---+ \n  O  \n /|\ \n     \n ==="
        HANGMAN3 = "+---+ \n  O  \n /|  \n     \n ==="
        HANGMAN2 = "+---+ \n  O  \n /   \n     \n ==="
        HANGMAN1 = "+---+ \n  O  \n     \n     \n ==="
        HANGMAN0 = "+---+ \n     \n     \n     \n ==="
        if self.num_lives == 6:
            print(HANGMAN6)
        elif self.num_lives == 5:
            print(HANGMAN5)
        elif self.num_lives == 4:
            print(HANGMAN4)
        elif self.num_lives == 3:
            print(HANGMAN3)
        elif self.num_lives == 2:
            print(HANGMAN2)
        elif self.num_lives == 1:
            print(HANGMAN1)
        elif self.num_lives == 0:
            print(HANGMAN0)

def play_game(word_list, num_lives, category):
    
    game = Hangman(word_list, num_lives)
    print(category)
    while True:
        if game.num_lives == 0:
            print("you lost!")
            print(f"The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif not game.num_letters >0 and game.num_lives != 0:
            print("congratulations")
            print(f"The word is {game.word}")
            break
        else:
            break


if __name__ == '__main__':
    
    print("Welcome to Hangman!")
    while True:
        play = input("Please enter y to play the game: \n Enter n to exit the game \n")
        if play == 'y':
            while True:
                difficulty = int(input("Please Choose a difficulty - \n Enter 1 for easy \n Enter 2 for medium \n enter 3 for hard: \n "))

                if difficulty == 1: #easy difficulty options
                    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon', 'kiwi', 'avocado', 'blueberry', 'grapes']
                    num_lives = 6
                    category = "the category is fruits"
                    play_game(word_list, num_lives, category)
                    break
                elif difficulty == 2: #medium difficulty options
                    word_list = ['brasilia', 'florence', 'lucknow', 'cambridge', 'reykjavik', 'cairo', 'moscow','helsinki','stockholm','washington']
                    num_lives = 5
                    category = "The category is places"
                    play_game(word_list, num_lives, category)
                    break
                elif difficulty == 3: #hard difficulty options
                    word_list = ['flabbergasted', 'indestructible', 'archaeological', 'businesses', 'agoraphobia', 'impossible','pharaoh','narcissistic','conscience','pronunciation']
                    num_lives = 4
                    category = "the category is words"
                    play_game(word_list, num_lives, category)
                    break
                else:
                    print("Invalid input")
            print("Please input if you want to replay or exit the game")
        
        elif play == 'n':
            print("Goodbye!")
            break

        else:
            print("Inavalid input, please choose from the options given")
   
   
