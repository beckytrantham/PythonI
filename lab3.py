#Reads the temperature in F from the keyboard, then prints the equivalent in C.
#Formula C = 5 / 9 * (F - 32)

temp = raw_input('What is the temperature in degrees Fahrenheit? ')
ftemp = float(temp)
ctemp = 5.0 / 9.0 * (ftemp - 32)
print 'The temperature is {} degrees Centigrade.' .format(ctemp)
