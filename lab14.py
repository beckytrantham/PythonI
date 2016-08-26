# Read trees.dat file
# Produce report showing
    # The number of trees in the sample
    # average height to on decimal
    # tallest
    # shortest
    # number of trees > 300
# Format for a professional report
tree_count = 0
tallest = 0
shortest = 1000
total_height = 0
num_under_300 = 0

fin = open('C:\\Users\\becky\\Desktop\\Python 1 Lab Mess\\trees.dat', 'r')
for linein in fin:
    tempheight = linein
    try:
        height = float(tempheight)
    except ValueError:
        print "Value Error. Height wasn't a number."
    else:
        tree_count += 1
        total_height = total_height + height
        if height > tallest:
            tallest = height
        if height < shortest:
            shortest = height
        if height < 300:
            num_under_300 += 1
average_height = total_height / tree_count    
fin.close()

target = open('C:\\Users\\becky\\Desktop\\Python 1 Lab Mess\\lab16 output', 'w')
target.write ("Tree Stats:")
target.write("\n")
target.write ("There are {} trees." .format(tree_count))
target.write("\n")
target.write ("The tallest tree is {:.0f} feet tall." .format(tallest))
target.write("\n")
target.write ("The shortest tree is {:.0f} feet tall." .format(shortest))
target.write("\n")
target.write ("The average height of the trees is {:.1f} feet." .format(average_height))
target.write("\n")
target.write ("There are {} trees under 300 feet tall." .format(num_under_300))
target.close()
