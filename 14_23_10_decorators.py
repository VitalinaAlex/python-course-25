"""Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!"""
#add called with 4, 5

def logger(func):
    def insidelogger(*args):
        print(f"{func.__name__} called with args= {args}")
        return func(*args)
    return insidelogger

@logger
def add(x, y):
    return x + y
 
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(2, 5))
print(square_all(2, 5, 7, 8, 9,58))

"""Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function"""

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            sentense = result.split()
            newsentense = []
            print(f"Sentense : {result}")
            print(f"Words in sentense : {sentense}")
            print(f"Stop words : {words}")
            for s in sentense:
                if s.strip("!,.?").lower() in [w.lower() for w in words]:
                    newsentense.append("*")
                else:
                    newsentense.append(s)
            new_sentence = ' '.join(newsentense)
            print(new_sentence)
            return new_sentence          
        return wrapper
    return decorator
    
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Steve")

#assert create_slogan("Steve") == "Steve drinks * in his brand new *!

"""Task 3
Write a decorator 'arg_rules' that validates arguments passed to the function.
A decorator should take 3 arguments:

max_length: 15
type_: str
contains: []  - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result."""

"""
def arg_rules(type_: type, max_length: int, contains: list):

    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'"""