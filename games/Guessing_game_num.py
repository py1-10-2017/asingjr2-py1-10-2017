#Number Guessing GAme
#Random number is generated, user has 6 guess to guess correct.
import random

def guess_game():
	counter = 1
	num = random.randint(0,21)
	name = raw_input("What is your your name")
	print 'Well ', name, "I am thinking of a number between 1 and 20.  Can you guess."
	guess = raw_input('Your guess is: ')
	guess = int(guess)
	while counter < 7:
		if guess < num:
			print "Your number is too low!  Please guess again"
			match = 'no'
		if guess > num:
			print "Your number is too low!  Please guess again"
			match = 'no'
		if guess == num:
			match = 'yes'
		if match == 'yes':
			print 'SUCCESS!!!  YOU GUESSED CORRECTLY IN ONLY {} guess(es)'.format(counter)
			break
		else:
			guess = raw_input('Please guess again ')
			guess = int(guess)
			counter += 1
        if counter == 6:
            print 'Sorry, you ran out of guesses.  The number I was thinking of was', str(num)
            break 

guess_game()
