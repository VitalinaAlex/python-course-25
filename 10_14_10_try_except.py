"""Task 1
Write a function called oops that explicitly raises an IndexError exception when called. 
Then write another function that calls oops inside a try/except state­ment to catch the error. 
What happens if you change oops to raise KeyError instead of IndexError?"""
def oops():
    raise IndexError("помилка IndexError!")

def handle_error():
    try:
        oops()
    except IndexError as e:
        print("Помилка перехоплена:", e)
        
handle_error()
#Помилка перехоплена: помилка IndexError!

def oops():
    raise KeyError("помилка KeyError!")

def handle_error():
    try:
        oops()
    except IndexError as e:
        print("Помилка перехоплена:", e)
        
handle_error()
#Traceback (most recent call last):
#KeyError: 'помилка KeyError!'

"""Task 2
Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
and then returns the value of squared a divided by b, construct a try-except block which catches an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero)."""
try:
    a = int(input('A = '))
    b = int(input('B = '))
    print(a**2 / b)
    
except ValueError:
    print("Wrong value")
    
except ZeroDivisionError:
  print("Zero division error")
