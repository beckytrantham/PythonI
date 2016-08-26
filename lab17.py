two_count = 0
seven_count = 0
import random
for i in range(1, 1001):
    roll = random.randrange(1, 7) + random.randrange(1, 7)
    if roll == 2:
        two_count += 1
    if roll == 7:
        seven_count += 1
percent_two = (two_count / 1000.0) * 100
percent_seven = (seven_count / 1000.0) * 100

print "{}% of the rolls were twos." .format(percent_two)
print "{}% of the rolls were sevens." .format(percent_seven)
