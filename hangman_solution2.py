from operator import truediv
import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        pass
        # initiaise wordlist 
        word_list=[]
        self.word_list=word_list
        # initialise numlives
        self.num_lives=num_lives
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
        letter=letter.lower()
        # check if the letter is in the word: 
            # print (letter is in the word)
        if letter in word:
           print("letter is in the word")

        for i in word:
            if letter==word[i]:
                


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



# %%
