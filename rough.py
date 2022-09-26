
import random
import string


#milestone 2
#word_list = ['apple','banana','kiwi','avocado','orange']
#print(word_list)
#word = random.choice(word_list)
#print(word)
"""guess = input("Please enter a character")
print(guess)
if len(guess)==1 and guess.isalpha:
    print("good guess")
else:
    print("Oops! That is not a valid input")"""


#milestone 3 
""""
while True:
    guess = input("Please enter a character")
    if len(guess)==1 and guess.isalpha:
        print("good guess")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again")
"""


""" while True:
        if len(guess)==1 and guess.isalpha and guess in word:
            print(f"Good guess! {guess} is in the word.")
            break
        elif len(guess)==1 and guess.isalpha and guess not in word:
            print(f"Sorry, {guess} is not in the word. Try again")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")"""



"""def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")
check_guess

check_guess = check_guess(word)
    

def ask_for_input():
    while True:
        guess = input("Please enter a character ")
        if len(guess)==1 and guess.isalpha():
            print("good guess")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()"""

#works perfect until now
#milestone 4

class Hangman:

    def __init__(self, word_list, num_lives):
        pass
        self.word = random.choice(word_list)
        self.word_guessed = ["_" * len(self.word)]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        #self.word_guessed2 = []

        print(f"The mystery word has {len(self.word)} characters")
        print(self.word_guessed)


    #creating method for checking letter
    def check_guess(self, guess):
    
        #guess = guess.lower() #redundant
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            """for i in range(len(self.word)):
                if self.word[i]==guess:
                    
                    self.word_guessed.append(guess)
                    print(self.word_guessed)"""
            for x, element in enumerate(self.word_guessed):
                if guess == element:
                    self.word_guessed[x] = element
                
            #self.word_guessed2 = ' '.join(self.word_guessed)
            print(self.word_guessed)
            self.num_letters -=1
        else:
            self.num_lives -=1
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

def play_game(word_list, num_lives):
    
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("you lost!")
            print(f"The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif not game.num_letters >0 and game.num_lives != 0:
            print("congratulations")
            print(f"The word was {game.word}")
            break
        else:
            break


if __name__ == '__main__':
    while True:
        difficulty = int(input("Welcome to Hangman! Please Choose a difficulty - \n Enter 1 for easy \n Enter 2 for medium \n enter 3 for hard"))

        if difficulty == 1:
            word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
            play_game(word_list, num_lives=5)
            break
        elif difficulty == 2:
            word_list = ['switzerland', 'florence', 'lucknow']
            play_game(word_list, num_lives=4)
            break
        elif difficulty == 3:
            word_list = ['flabbergasted', 'indestructible']
            play_game(word_list, num_lives=3)
            break
        else:
            print("Invalid input")
            

    
        


# %%
