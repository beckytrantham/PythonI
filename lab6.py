#Reads the temperature in F from the keyboard, then prints the equivalent in C.
#Formula C = 5 / 9 * (F - 32)

while True:
    temp = raw_input('What is the temperature in degrees Fahrenheit? ')
    if temp == 'q' or temp == 'Q':
        break
    ftemp = float(temp)
    ctemp = 5.0 / 9.0 * (ftemp - 32)
    print 'The temperature is {} degrees Centigrade.' .format(ctemp)
    if ftemp > 95:
        print "It's very hot outside."
    elif ftemp > 80:
        print "It's hot."
    elif ftemp > 60:
        print "It's nice out."
    elif ftemp > 40:
        print "It's chilly."
    else: 
        print "It's cold!"
    
