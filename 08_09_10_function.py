"""Task 1
A simple function.
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
The function should then print "My favorite movie is named {name}"."""

 def favorite_movie(film_name):
    print(f"My favorite movie is named {film_name}")

film_name=input("Enter your favorite movie: ")
favorite_movie(film_name)

"""Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
Make the function print out the values of the dictionary to make sure that it works as intended."""

def make_country(name,capital):
    print(f"{name} -> {value}")

country_dict = {
    "Ukraine": "Kyiv",
    "Poland": "Warsaw",
    "Germany": "Berlin",
    "Slovakia": "Bratislava"
}
for key, value in country_dict.items():
    make_country(key, value) 

"""Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. For example:
the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42 """

def make_operation(operator, *parameters):
    if not parameters:
        return 0

    result = parameters[0]
    for number in parameters[1:]:
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        else:
            raise ValueError("Unknown operator")
    print(result)

make_operation("+", 7, 7, 2)
make_operation("-", 5, 5, -10, -20)
make_operation("*", 7, 6)
# option 2
import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
def make_operation(operator, *parameters):
    op = ops.get(operator)
    if not op:
        raise ValueError("Unknown operator")
    result = parameters[0]
    for num in parameters[1:]:
        result = op(result, num)
    print(result)
    
make_operation("+", 7, 7, 2)
make_operation("-", 5, 5, -10, -20)
make_operation("*", 7, 6)
