
import random
import string

"""from operator import truediv
import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        pass
        # initiaise wordlist 
        word_list=[]
        self.word_list=word_list
        # initialise numlives
        num_lives=5
        # initialise word
        word=""
        # initialise word guessed 
        word_guessed=[]
        self.word_guessed=word_guessed
        # initialise numlives 
        self.num_lives=num_lives
        # initialise list letters 
        list_letters=[]
        print("The mystery word has {len(self.word)} characters")
        print(word_guessed)

    def check_letter(self, letter):
        pass
        # change letter to lowercase and assign to variable called letter
        #%%
        letter=letter.lower()
        # check if the letter is in the word: 
            # print (letter is in the word)
        if letter in word:
           print("letter is in the word")

        for i in word:
            if letter==word[i]:
                word[i]=letter
                print(word)
                """"""
            else:
                num_lives=num_lives-1
            list_letters= list_letters.append(letter)

            #range function, letter = index of word
            # 





        # create a for loop that checks for the position and character of the letters in the word:
            #check if the character == letter:
                # assign the letter to the word guessed at that position
                #print the word guessed 
                # reduce the numbr of letters by 1 
            #else:
                #reduce number of lives by 1
            # append the letter into the list of letters 



            


    def ask_letter(self):
        pass
        #take an input from the user and asssign it to letter
        #%%
        
        letter=input("Please enter a letter")
        #check if len(letter)!=1 and not letter.isalpha: 
        # enter the correct input
        if len(letter)!=1 or not letter.isalpha:
            letter=input("Please, enter just one character")
            #check if the letter has been already tried (in the list of letters):
            # print (that letter has already been tried)
        if letter in list_letters:
            print( "the letter" + letter + "has already been tried")
            letter=input("Please enter a single letter that you have not already tried")
        #call check letter method (letter as an argument)    
        check_letter(letter)
   

def play_game(word_list):
    # create an instance of the class
    ask_letter(self)
    
    pass
    game = Hangman(word_list, num_lives=5)

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

"""





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
            

       
    """"
    while True:
        play_again = input("Please enter Y to play again at the same difficulty \n Enter N to exit the game \n if you want to change the difficulty please exit and re-start the game: \n ").lower()
        if play_again == 'y':
            play_game(word_list, num_lives, j)
            
        elif play_again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input")
"""
        


# %%
