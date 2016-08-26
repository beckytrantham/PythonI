# Function simulating rolling a pair of dice
# First roll 7 or 11 = win
# First roll 2, 3, or 12 = loss
# Any other number = the Point and you must roll again
# On subsequent rolls:
#    7 = loss
#    the Point = win 
#    Any other number = reroll
# Start with $100 and bet $10 each play
# Print all the rolls and whether you have won or lost on one line.
# Print the funds balance and a request to play again on the line.
# 'y' or 'Y' means play again, anything else ends play.
# A balance of $0 ends play automatically.
# Show numyber of plays when they end play.

import random
def dice_roll():
    roll = random.randrange(1, 7) + random.randrange(1, 7)
    print roll,
    return roll

def win(balance):
    balance = balance + 20
    print " You win!" 
    print "Balance = ${}" .format(balance)
    return balance

def lose(balance):
    ready = 'n'
    print " You lose." 
    if balance > 0:
        print "Balance = ${}" .format(balance)

def play(balance):
    balance = balance - 10
    roll = dice_roll()
    if roll == 7 or roll == 11:
       balance = win(balance)
    elif roll == 2 or roll == 3 or roll == 12:
        lose(balance)
    else:
        point = roll
        roll = dice_roll()
        while roll != 7 and roll != point:
            roll = dice_roll()
        if roll == 7:
                lose(balance)
        elif roll == point:
               balance = win(balance)
    return balance
                    
# Initialize starter values and ask if player is ready.
plays = 0
balance = 100
ready = raw_input("Ready to roll? y/n: ")

while (ready == 'y' or ready == 'Y') and balance > 0:
    balance = play(balance)
    plays += 1
    if balance > 0:
        ready = raw_input("Play again? y/n: ")
print "Number of plays = {}" .format(plays)
print "Ending Balance = ${}." .format(balance)
        

            
            
            







    

