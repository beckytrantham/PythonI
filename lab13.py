#Converts temperature in Fahrenheit to Centigrade
#Formula: C = 5/9 *(F-32)
#Use Try statement to catch ValueError exceptions
#Use file as a data source instead of raw_input()

def f_to_c(ftemp):
    return 5.0 / 9.0 * (ftemp - 32)

fin = open('C:\\Users\\becky\\Desktop\\Python 1 Lab Mess\\temps.dat', 'r')
for linein in fin:
    temp = linein
    try:
        ftemp = float(temp)

    except ValueError:
        print "Value Error. You did not enter a number."

    else:
        ctemp = f_to_c(ftemp)
        print "The temperature is {0} degrees Fahrenheit and {1} degrees Centigrade." .format(ftemp, ctemp)
fin.close()
