#Converts temperature in Fahrenheit to Centigrade
#Formula: C = 5/9 *(F-32)

def f_to_c(ftemp):
    return 5.0 / 9.0 * (ftemp - 32)

temp = raw_input("What is the temperature in degrees Fahrenheit? ")
ftemp = float(temp)

ctemp = f_to_c(ftemp)
print "The temperature is {0} degrees Fahrenheit and {1} degrees Centigrade." .format(ftemp, ctemp)
