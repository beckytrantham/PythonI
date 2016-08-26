#Converts temperature in Fahrenheit to Centigrade
#Formula: C = 5/9 *(F-32)
#Use Try statement to catch ValueError exceptions

def f_to_c(ftemp):
    return 5.0 / 9.0 * (ftemp - 32)

temp = raw_input("What is the temperature in degrees Fahrenheit? ")
try:
    ftemp = float(temp)

except ValueError:
    print "Value Error. You did not enter a number."

else:
    ctemp = f_to_c(ftemp)
    print "The temperature is {0} degrees Fahrenheit and {1} degrees Centigrade." .format(ftemp, ctemp)
