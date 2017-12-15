#Purpose of game is for user to what a word is based on jumble of letters
#User can ask for a random hint from a selection of hints
import random

def mixup(word):
    new_word = ''
    word = list(word)
    for i in range(len(word)):
        pick = random.choice(word)
        if pick in word:
            new_word += pick
            word.remove(pick)
    return new_word

try:
    jum_word = mixup(word)
    if jum_word == word:
        jum_word = mixup(jum_word) #not perfect for short words
except:
    pass

def word_choice():
    color_word_list = ['Red', 'Brown', 'Purple', 'Alabaster', 'Amber', 'Violet', 'Cyan']
    animal_word_list = ['deer', 'bat', 'eagle', 'raven', 'giraffe', 'beettle', 'ram']
    possible_lists = [color_word_list, animal_word_list]
    word = random.choice(random.choice(possible_lists))
    print jum_word        
    len_word = len(word)
    word_first = str(word[0])
    word_last = str(word[int(len_word)-1])
    hint_1 = 'The word has {} letters'.format(len_word)
    hint_2 = 'The first letter of the word is {}'.format(word_first.lower())
    hint_3 = 'The last letter of the word is {}'.format(word_last.lower())
    hint_choices = [hint_1, hint_2, hint_3]
    hc = random.choice(hint_choices)
    print '''
    Let\'s play a guessing game.
    You will get three chances to guess a word.
    Good luck!
    '''
    guess_counter = 0
    match = 'No'
    if guess_counter < 4:
        should_play = True
    def guessing():
        guess_counter += 1
        print jum_word
        guess = raw_input('Your guess is: ')
        guess = guess.lower()
        return guess

    # def eval(guess):
    if guess == word:
        match = 'yes'
        if guess != word:
            match = 'no'
        if match == 'yes':
            print 'Well done!  You guessed the word!!!!'
        if match == 'no':
            print 'Sorry!  Your guess was off'
            hint_choice = True 
            while hint_choice:
                hint = raw_input("Would you like a hint?  Y or N? ")
                if hint == 'Y':
                    print hc
                    hint_choice = False
                elif hint == 'N':
                    hint_choice = False
                else:
                    print 'Sorry, you must type Y or N and press enter.'

word_guess() 

    # playing()
    # guess = raw_input('Your next guess is: ')
    #     if guess == word:
    #         match = 'yes'
    # if guess != x:
    #     match = 'no'
    # if match = 'yes':
    #     print 'Well done!  You guessed the color!!!!'
    # if match = 'no':
    #     print 'Sorry!  Your guess was off'
    #     hint_choice = True 
    #     while hint_choice:
    #     hint = raw_input(prompt="Would you like a hint?  Y or N? ")
    #         if hint == 'Y':
    #             print hint_1
    #             hint_choice = False
    #         elif hint == 'N':
    #             hint_choice = False
    #         else:
    #             print 'Sorry, you must type Y or N and press enter.'
        
    # print x_first
    # print x_last
    # print hint_1
    # print hint_2
    # print hint_3
    # print x
    # return x

