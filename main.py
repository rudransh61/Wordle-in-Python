# dependencies
import random 
import os
from strings import *

#loading 5 letter words from file
words = ['hello','black','chick','sigma','apple','fruit','seven','voice','maths']


#answer
answer = random.choice(words)
# print(answer)

#input array 
inputs = []


#game variables
num = 0
won = False
guessed = False

while num!=5 and won==False and guessed==False:

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