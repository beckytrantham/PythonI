print "Opening the file..."
target = open('C:\\Users\\becky\\Desktop\\Python 1 Lab Mess\\lab15 output', 'w')

line1 = "I'm practiing writing a file with python."
line2 = "I'm glad I get to do this at home."
line3 = "I'm almost ready for level 2."

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
