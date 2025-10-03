"""Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. 
The result should be sent back to the user via a print statement."""
import random
randomizer=random.randint(1,10)
max = 10
element=1
enterednumber=None
while element <= max:
    try:
        enterednumber=int(input(f"Attempt {element}. Let's try to guess the number..."))
        if randomizer == enterednumber:
            print(f"YOU ARE RIGHT!!! It's {randomizer}")
            print(f'It took you {element} tries to guess correctly.')
            break
        element += 1
    except ValueError:
        print("Invalid number format!")
else:
 print(f"You've run out of chances :( Guessed number = {randomizer}") 

"""Task 2
The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years” """  
greetingname = None
greetingname = input("What is your name?...")
greetingage = None
try:
    greetingage = int(input("How old are YOU?..."))
    if greetingage > 0:
        print(f"Hello {greetingname}, on your next birthday you’ll be {greetingage+1} years!")
    else:
        print(f"Hello {greetingname}, You haven't been born yet ;) !")
except ValueError:
    print(f"{greetingname}, Invalid number format!") 

"""Task 3
Words combination
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)"""
import random
my_string = input('Input string...')
length=len(my_string)
if length >= 5:
    for i in range(5):
        print(f'\nWord # {i+1}',end=' - ')
        for j in range(5):
            random_char = random.choice(my_string)
            print(random.choice(my_string),end='')
else:
    print('\nNot enough characters for a sufficient number of combinations')
print(f'\nThe string is = {my_string}')
