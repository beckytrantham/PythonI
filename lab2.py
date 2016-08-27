#Lab 1 Part 1
buy_price = 25.32
sell_price = 48.97
shares = 125

profit = (shares * sell_price) - (shares * buy_price)
print "The profit is: ${:,.2f}" .format(profit)

#Lab 1 Part 2
original_price = 127.99
sale_price = (1-.16) * original_price
print "The sale price is: ${:.2f}" .format(sale_price)

#Raw Input Exercise
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
