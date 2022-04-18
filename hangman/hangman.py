#Hangman read from file
#random word
import random
from words import word_list

print("Hangman Game")

#opens py word doc

random_word = random.choice(word_list)
length = len(random_word)
dashed_word = ('_ ' * length).split()
guesses = 6
used = []

#loop random word + ask user for letter
while True:
    print (' '.join(dashed_word))
    letter = input('Enter Letter: ')

    #subtract guesses if wrong letter
    if (letter not in random_word):
        if letter not in used:
            guesses -= 1
            used.append(letter)

            #wrong answer + showing random word
            if guesses == 0:
                random_word = random_word.upper()
                print('You got it wrong, the word was: ', random_word)
                break

            #print number of guesses and wrong letters used
            print ('Try again, you have %r guesses left!'  %guesses)
            print('You have used:')
            print(used)

    #checks if letter is in string and replaces dash with letter
    else:
        for i in range(length):
            if letter == random_word[i]:
                dashed_word[i] = letter

    #correct random word
    if (''.join(dashed_word) == random_word):
        random_word = random_word.upper()
        print ('Nice you got it! The word was: '  + random_word)
        break










