"""Task 1
School
Make a class structure in python representing people at school. Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes, and keep in mind which are common and which are not. 
For example, the name should be a Person attribute, while salary should only be available to the teacher."""

class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def whoiam(self):
        return "I’m a person."

person1 = Person("Olga", "Women")
print (f"{person1.name} is a {person1.sex}")
print(person1.whoiam())

class Student(Person):
    def __init__(self, name, age, grade, subject):
        super().__init__(name, age)
        self.grade = grade
        self.subject = subject

    def whoiam(self):
        return "I’m a student."

student1 = Student("Willy", "Men", 12, "math")
print (f"{student1.name} is a {student1.sex} with {student1.grade} grade on {student1.subject}")
print(student1.whoiam())

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def whoiam(self):
        return "I’m a teacher."

teacher1 = Teacher("Lily", "Women", "math", 50000)
print (f"{teacher1.name} is a {teacher1.sex} with {teacher1.salary} salary for {teacher1.subject}")
print(teacher1.whoiam())

"""Task 2
Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years' """

class Mathematician:
    def square_nums(self, numbers):
        return list(map(lambda x: x * x, numbers))
    def remove_positives(self, numbers):
        return list(filter(lambda x: x < 0, numbers))
    def filter_leaps(self, numbers):
        return list(filter(lambda x: ((x % 4==0) and (x % 100 !=0) or ( x % 400==0)), numbers))

m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
print(m.square_nums([7, 11, 5, 4]))
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
print(m.remove_positives([26, -11, -8, 13, -90]))
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

"""
Task 3
Product Store
Write a class Product that has three attributes:
type, name, price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). 
    The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. 
    It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store."""
import json
import os

class Product:
    def __init__(self, typeofproduct, name, price):
        self.typeofproduct = typeofproduct
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.income = 0
        self.file_name = "store_data.json"
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                self.products = json.load(f)
        else:
            self.products = {}
"""            
    def add(self, product, amount):
        pass
    def set_discount(self, identifier, percent, identifier_type=’name’):
        pass
    def sell_product(self, product_name, amount):
        pass
    def get_income(self):
        pass
    def get_all_products(self):
        pass
    def get_product_info(self, product_name):
        pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)"""
"""
Task 4
Custom exception
Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its functionality to log every error message to a file named 'logs.txt'. 
Tips: Use __init__ method to extend functionality for saving messages to file


class CustomException(Exception):

def __init__(self, msg): """
