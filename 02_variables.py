#Task 1
#The greeting program.
#Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
#     "Good day <name>! <day> is a perfect day to learn some python."
#Note that  <name> and <day> are predefined variables in source code.
#An additional bonus will be to use different string formatting methods for constructing result string.
from datetime import datetime
name='Vitalina'
today=datetime.now()
print("\033[32mGood day",name,"!", today.strftime("%a,%b %d,%Y")," is a perfect day to learn some python.\033[0m")
#Task 2
#Manipulate strings.
#Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
first_name='Vitalina'
second_name="Aleksieienko"
print(first_name,second_name)
FIO = first_name + " " + second_name
print(FIO)
first_last=[first_name,second_name]
separator=" "
FIO_2 = separator.join(first_last)
print(FIO_2)#Task 3
#Using python as a calculator.
#Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 
valueA=126
valueB=-10.6
#Addition
print("valueA+valueB=",valueA+valueB)
#Subtraction
print("valueA-valueB=",valueA-valueB)
print("valueB-valueA=",valueB-valueA)
#Division
print("valueB/valueA=",round(valueB/valueA,2))
print("valueA/valueB=",round(valueA/valueB,2))
#Multiplication
print("valueB*valueA=",valueB*valueA)
#Exponent (Power)
print("valueB^valueA=",pow(valueB,valueA))
print("valueA^valueB=",pow(valueA,valueB))
#Modulus
print(f"Модуль {valueA}: {abs(valueA)}")
print(f"Модуль {valueB}: {abs(valueB)}")
#Floor division
print(f"1/{valueA}={round(1/valueA,4)}")
print(f"1/{valueB}={round(1/valueB,4)}")
