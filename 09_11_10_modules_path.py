"""Task 1
Imports practice
Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice."""
#Файл module_1.py
def function_in_module1():
    print("You are in the module number 1")
    
function_in_module1() 
# Файл module_2.py
import module_1

"""Task 2
The sys module.

The “sys.path” list is initialized from the PYTHONPATH environment variable. 
Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out."""
import sys
print(sys.path)
#['/Users/macbook/Desktop/Пітон', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', '/Users/macbook/Library/Python/3.10/lib/python/site-packages', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages'] 

sys.path.append('/Users/BEETROOT/my_modules')
#'/Users/macbook/Desktop/Пітон', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', '/Users/macbook/Library/Python/3.10/lib/python/site-packages', '/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages', '/Users/BEETROOT/my_modules']
"""Task 3

Basics, import, work with os module
Write a program that counts lines and characters in a file (similar to `wc` Unix-utility, for additional info about it follow the link: 
https://www.geeksforgeeks.org/wc-command-linux-examples/ or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).
Create a Python module called "mymod.py", which has three functions:

count_lines(name) function that reads an input file and counts the number of lines in it (hint: file.readlines() does most of the work for you, and "len" does the rest) 
count_chars(name) function that reads an input file and counts the number of characters in it (hint: file.read() returns a single string)
test(name) function that calls both counting functions with a given input file­name. 
Such a filename generally might be passed-in, hard-coded, input with input(), or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
All three `mymod.py` functions should expect a filename string to be passed in. 

Test your module interactively, using import and name qualification to fetch your exports. 
Does your PYTHONPATH need to include the directory where you created mymod.py?

Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice; if you’re feeling ambitious, 
you may be able to improve this by passing an open file object into the two count functions (hint: file.seek(0) is a file rewind)."""
def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        print(len(lines))
        return len(lines)
    
def count_chars(name):
    with open(name, 'r') as file:
        text = file.read()
        print(len(text))
        return len(text)
    
def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Файл '{name}' має {lines} рядків і {chars} символів.")   

count_lines("README-RUS.txt")
count_chars("README-RUS.txt")
test("README-RUS.txt")
test("mymod.py")

def count_lines(file):
    return len(file.readlines())

def count_chars(file):
    return len(file.read())

def test(name):
    with open(name, 'r', encoding='utf-8') as f:
        lines = count_lines(f)
        f.seek(0)
        chars = count_chars(f)
    print(f"Файл '{name}' має {lines} рядків і {chars} символів.")
    
test("README-RUS.txt")
test("mymod.py")

#36
#2196
#Файл 'README-RUS.txt' має 36 рядків і 2196 символів.
#41
#903
#Файл 'mymod.py' має 41 рядків і 903 символів.
#Файл 'README-RUS.txt' має 36 рядків і 2196 символів.
#Файл 'mymod.py' має 41 рядків і 903 символів.""
