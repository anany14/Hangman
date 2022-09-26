import random
import string
class Hangman:

    def __init__(self, word_list, num_lives):
        pass
        self.word = random.choice(word_list)
        self.word_guessed = ["_" * len(self.word)]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.word_guessed_list = list(self.word_guessed)
        HANGMAN6 = "+---+ \n  O  \n /|\ \n / \ \n ==="
        


        print(f"The mystery word has {len(self.word)} characters")
        print(HANGMAN6)
        print(self.word_guessed)


    #creating method for checking letter
    def check_guess(self, guess):
        
        HANGMAN5 = "+---+ \n  O  \n /|\ \n /   \n ==="
        HANGMAN4 = "+---+ \n  O  \n /|\ \n     \n ==="
        HANGMAN3 = "+---+ \n  O  \n /|  \n     \n ==="
        HANGMAN2 = "+---+ \n  O  \n /   \n     \n ==="
        HANGMAN1 = "+---+ \n  O  \n     \n     \n ==="
        HANGMAN0 = "+---+ \n     \n     \n     \n ==="

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            
            for x, element in enumerate(self.word_guessed):
                if guess == element:
                    self.word_guessed[x] = element
                
            self.word_guessed_list = ' '.join(self.word_guessed)
            print(self.word_guessed_list)
            self.num_letters -=1
        else:
            self.num_lives -=1
            
            if self.num_lives == 5:
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
            
            print(f"Sorry, {guess} is not in the word. Try again")
            print(f"You have {self.num_lives} tries left")

        self.list_of_guesses.append(guess)

    #method for input
    def ask_for_input(self):
        pass
        s = set(string.ascii_lowercase) #making a set of lower case alphabets for the elif statements
        while True:
            guess = input("Please enter a character ")
            guess = guess.lower() #converting into lowercase letters to compare to s
            if len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess not in s:
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

def play_game(word_list, num_lives, j):
    
    game = Hangman(word_list, num_lives)
    print(j)
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
    while True:
        difficulty = int(input("Welcome to Hangman! Please Choose a difficulty - \n Enter 1 for easy \n Enter 2 for medium \n enter 3 for hard "))

        if difficulty == 1: #easy difficulty options
            word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
            num_lives = 6
            j = "the category is fruits"
            play_game(word_list, num_lives, j)
            break
        elif difficulty == 2: #medium difficulty options
            word_list = ['brasilia', 'florence', 'lucknow', 'cambridge', 'reykjavik', 'cairo']
            num_lives = 5
            j = "The category is places"
            play_game(word_list, num_lives, j)
            break
        elif difficulty == 3: #hard difficulty options
            word_list = ['flabbergasted', 'indestructible', 'archaelogical', 'businesses', 'agrophobia', 'impossible']
            num_lives = 4
            j = "the category is words"
            play_game(word_list, num_lives, j)
            break
        else:
            print("Invalid input")
    
    while True:
        play_again = input("Please enter Y to play again at the same difficulty \n Enter N to exit the game \n if you want to change the difficulty please exit and re-start the game ").lower()
        if play_again == 'y':
            play_game(word_list, num_lives, j)
            
        elif play_again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input")
