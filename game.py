"""A number-guessing game."""
from random import *
# Put your code here
name = raw_input('Hello, what is your name: ')
print 'Hello, %s' % (name)
print '%s I am thinking of a number between 1 and 100, try to guess my number' % (name)
#guess = raw_input('What is your guess: ')
secret_num = randint(1, 100)
guess_count = 0

while True:
    try:
        guess = int(raw_input("Please enter a number: "))
        # continue
    except:
        print "That was not a number. Please try again!"

 while True: 
    if guess <= 100 and guess >= 1:
        #print 'Good job, let us see if it is close to the secret number'
        if guess > secret_num:
            print 'Your guess is too high, please try again.'
            break
        elif guess < secret_num:
            print 'Your guess is too low, please try again.'
            break
        else:
            print 'Congratulations %s! You found my number in %s tries!' % (name, guess_count)
            break
        guess_count += 1
    else:
        print "Please choose a number between 1 and 100."
        break 
        



         #add guess counter



