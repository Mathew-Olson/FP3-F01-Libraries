#-------------------------------
# FP3 - Formative #1 - Libraries
# Mathew Thomas Olson
# 11 April 2024
#-------------------------------
###imports###
import time
from external import Formulas
from external import printing

###main code###
active = input("would you like to convert some temps? ")

while active == "yes": #I also managed to make it repeatable.
    choice = input(" 1 for celcius to farenheit, 2 for farenheit to celcius. ")
    time.sleep(1)

    if choice == "1":
        number = int(input("what number are you converting. "))
        time.sleep(1)
        new_temp = Formulas.c_to_f(number) #uses the Formulas file
        style = ("c to f")
        
    elif choice == "2":
        number = int(input("what number are you converting. "))
        time.sleep(1)
        new_temp = Formulas.f_to_c(number) #uses the Formulas file
        style = ("f to c")

    else:
        print("(inccorect format)")
        time.sleep(1)
        exit()
    
    printing.display(style, new_temp) #uses the printing file
    time.sleep(1)
    active = input("would you like to try again? ")

time.sleep(1)
print("Goodbye")
exit()