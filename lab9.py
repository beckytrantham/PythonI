import random
randomnumber = random.randrange(1, 101)
number = int(randomnumber)
guess = 0
attempts = 1
while guess != number:
    guess = raw_input ('Enter your guess: ')
    guess = int(guess)
    attempts = attempts + 1
    if guess < number:
        print "Your guess is too low."
    elif guess > number:
        print "Your guess is too high."
    elif guess == number:
        print "Your guess is correct!"
        print "You succeeded in %d attempts!" % attempts
