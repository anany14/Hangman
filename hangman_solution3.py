from operator import truediv
import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        pass
        word_list = []
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.list_letters = []
        self.num_letters = len(self.word)
        word_guessed = []
        """self.word_guessed = len(self.word) * ['_']
        self.word_guessed = ['_' for x in self.word]"""
        print(f"The Mystery word has {len(self.word)} characters {self.word_guessed}")

        print(self.word_guessed)

    
    def check_letter(self, letter): 
        pass


    def ask_letter(self):
        pass
        #%%
         #take an input from the user and asssign it to letter
        letter=input("Please enter a letter")
        #check if len(letter)!=1 and not letter.isalpha: 
        # enter the correct input
        if len(letter)!=1 or not letter.isalpha:
            print("Oops! That is not a valid input")
            letter=input("Please, enter just one character")
            #check if the letter has been already tried (in the list of letters):
            # print (that letter has already been tried)
        else:    
            if letter in list_letters:
                print(f"the letter {letter} has already been tried")
                letter=input("Please enter a single letter that you have not already tried")
        #call check letter method (letter as an argument)    
        #check_letter(letter)
   

def play_game(word_list):
    # create an instance of the class
    ask_letter(self)
    
    pass
    game = Hangman(word_list, num_lives=5)

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)

# %%
