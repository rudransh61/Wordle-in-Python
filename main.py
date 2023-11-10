# dependencies
import random 
import os
from strings import *

#loading 5 letter words from file
# words = ['hello','black','chick','sigma','apple','fruit','seven','voice','maths']
file_path = 'words.txt' 
with open(file_path, 'r') as file:
    words = [word.strip() for line in file for word in line.split() if len(word.strip()) == 5]

# Now 'words_with_length_5' contains a list of words from the file with length exactly equal to 5
# print(len(words))
# print(words)

#answer
answer = random.choice(words)
# print(answer)

#input array 
inputs = []


#game variables
num = 0
won = False
guessed = False

print("\Welcome to Wordle ! Predict the correct 5 letter word in 5 guesses  to WIN !! \n\-----Green : Correct letter in correct position \n\-----Yellow Correct Letter in Incorrect position  ")

while num!=6 and won==False and guessed==False:

    input_word = input('Type the word :')

    if input_word==answer :
        guessed = True

    
    correct ,diffpos =matchings_positions(input_word,answer)
    # print(correct,diffpos)
    print("Green : ")
    for i in correct:
        print("     ",i)
    
    print("Yellow : ")
    for i in diffpos:
        print("     ",i)
    
    num+=1



if guessed :
    print('Congrats !! You guessed it !! , \n the correct word is:-',answer)


else :
    print('Better Luck for next time \n the correct word is:-',answer)