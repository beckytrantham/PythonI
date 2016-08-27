#Reads the temperature in F from the keyboard, then prints the equivalent in C.
#Formula C = 5 / 9 * (F - 32)


for temp in range(-40, 111, 10):
    if temp == 0 or temp == 50:
        continue    
    ftemp = float(temp)
    ctemp = 5.0 / 9.0 * (ftemp - 32)
    print 'The temperature is {0} degrees Centigrade and {1} degrees Fahrenheit.' .format(ctemp, ftemp)

    
