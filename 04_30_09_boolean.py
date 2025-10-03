TEXT="""
Task 1
String manipulation
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: 'x'
Expected Result: Empty String
Tips:
Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters"""
my_string = input('Enter the String: ')
index=len(my_string)
print(f'String length :{index}')
minlength=2
if index >= second:
    final_string = my_string[0:minlength]+my_string[index-minlength:index]
else:
    final_string = ''
print(f'My string: {my_string}')
print(f'Final string: {final_string}')
TEXT="""
Task 2
The valid phone number program.
Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation."""
telnumber= input('Enter your mobile number: ')
length=len(telnumber)
if telnumber.isdigit():
    print('The number contains only digits.')
    if length == 10:
        print('The length of your number is right.')
    else:
        print('The length of the number is incorrect.')
else:
    print('The number contains not only digits.')
print(f'String length: {length}')
print(f'Your number: {telnumber}')

TEXT="""
Task 3
The math quiz program.
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly."""
firstdigit = None
seconddigit = None
try:
    firstdigit = float(input('Enter the first digit: '))
    seconddigit = float(input('Enter the second digit: '))
    answer= int(input(f'Sum of numbers {firstdigit} and {seconddigit} = '))
    if answer == firstdigit+seconddigit:
        print('YOU ARE RIGHT!!!')
    else:
        print(f"You're wrong. :( Sum = {firstdigit+seconddigit}")
except ValueError:
    print("Error: you must enter a number, not text!")
    print('Be more careful next time.')
print(f'A = {firstdigit}')
print(f'B = {seconddigit}')

TEXT="""
Task 4
The name check.
Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True."""
myname = 'vitalina'
inputname = ""
inputname = input('Hi! What is your name: ')
if myname == inputname.lower():
    print('YOU ARE RIGHT!!!')
else:
    print(f"You're wrong. :(")
print(f'My name = {myname}')
print(f'Input name = {inputname}')










