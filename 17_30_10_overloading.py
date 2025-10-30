from __future__ import annotations
"""Task 1
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: 
Dog and Cat, and make their own implementation of the method talk be different. 
For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter. """ 

from dbm.ndbm import library


class Animal:
    def __init__(self, kindofanimal, region):
        self.kindofanimal = kindofanimal
        self.region = region

    def talk(self):
        print(f"The {self.kindofanimal} lives at {self.region}")

class Dog(Animal):
    def __init__(self, kindofanimal, region, name, age):
        super().__init__(kindofanimal, region)
        self.name = name
        self.age = age

    def talk(self):
        result = (f"{Dog.__name__} said woof woof")
        print(result)

class Cat(Animal):
    def __init__(self, kindofanimal, region, name, age):
        super().__init__(kindofanimal, region)
        self.name = name
        self.age = age

    def talk(self):
        result = (f"{Cat.__name__} said meow")
        print(result)

def make_animal_talk(animal):
    animal.talk()

my_dog = Dog("mammal", "Europe","Charly", 6)
my_dog.talk()
my_cat = Cat("mammal", "Asia","Kitty", 2)
my_cat.talk()
my_animal = Animal("mammal", "Europe")
my_animal.talk()
make_animal_talk(my_dog)
make_animal_talk(my_cat)

"""Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books"""

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    
    def __str__(self):
        return self.name

class Book:
    book_count = 0
    def __init__(self, name, year, author):
        self.author = author
        self.name = name
        self.year = year
        Book.book_count += 1
        print(f"Кількість книжок {Book.book_count}. Додана книга {self.name},{author},{self.year}")
    
    def __repr__(self):
        return f"Book('{self.name}', {self.year}, {self.author.name})"

    def __str__(self):
        return f"{self.name} ({self.year}) by {self.author.name}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        newbook = Book(name, year, author)
        self.books.append(newbook)
        author.books.append(newbook)
        return newbook
        
    def group_by_author(self, author: Author):
        result = []
        for b in self.books:
            if b.author.name == author.name:
                result.append(b)
        return result

    def group_by_year(self, year: int):
        result = []
        for b in self.books:
            if b.year == year:
                result.append(b)
        return result

my_library = Library ("KPI")
author1 = Author("king", "USA", "22-05-1980")
book1 = my_library.new_book("Harry Potter", 1997, author1)
book2 = my_library.new_book("qwerty", 2021, author1)
book3 = my_library.new_book("ygggkgukuguk",2021,author1)

for book in my_library.group_by_author(author1):
    print(book)
for book in my_library.group_by_year(2021):
    print(book)

"""Task 3
Fraction
Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною перевіркою й обробкою помилок. 
Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction"""

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError ("the denominator cannot be equal to 0")

        if (numerator < 0) != (denominator < 0):
            self.numerator = -abs(numerator)
        else:
            self.numerator = abs(numerator)

        self.denominator = abs(denominator)

    def __add__(self, other: Fraction):
        first_num = self.numerator
        first_den = self.denominator
        other_num = other.numerator
        other_den = other.denominator
        new_num = first_num*other_den+other_num*first_den
        new_den = first_den*other_den
        return Fraction(new_num, new_den)

    def __sub__(self, other: Fraction):
        first_num = self.numerator
        first_den = self.denominator
        other_num = other.numerator
        other_den = other.denominator
        new_num = first_num*other_den-other_num*first_den
        new_den = first_den*other_den
        return Fraction(new_num, new_den)

    def __mul__(self, other: Fraction):
        first_num = self.numerator
        first_den = self.denominator
        other_num = other.numerator
        other_den = other.denominator
        new_num = first_num*other_num
        new_den = first_den*other_den
        return Fraction(new_num, new_den)    
    
    def __truediv__(self, other: Fraction):
        first_num = self.numerator
        first_den = self.denominator
        other_num = other.numerator
        other_den = other.denominator
        new_num = first_num*other_den
        new_den = first_den*other_num
        return Fraction(new_num, new_den)
    
    def __eq__(self, other: Fraction):
        first_num = self.numerator
        first_den = self.denominator
        other_num = other.numerator
        other_den = other.denominator
        new_num = first_num*other_den
        new_den = first_den*other_num
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    print(x + y)
    print(x - y)
    print(y - x)
    print(x * y)
    print(x / y)
    print (x == y)