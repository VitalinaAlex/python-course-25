"""Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor. 
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
Email validations:
Valid email address format 
Email address """
from string import ascii_letters, digits

class User:
    ukrainian_letters = "абвгґдеєжзийіїклмнопрстуфхцчшщьюя-'"
    ukrainian_letters_upper = ukrainian_letters.upper()
    ukrainian = ukrainian_letters + ukrainian_letters_upper

    def __init__(self, fio, email, city):
        self.validate_fio(fio)
        self.__fio = fio.split()
        self.validate_email(email)
        self.__email = email
        self.__city = city

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email (self, email):
        self.__email = email

    @email.deleter
    def email (self):
        del self.__email

    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio (self, fio):
        self.__fio = fio

    @fio.deleter
    def fio (self):
        del self.__fio

    @classmethod
    def validate_fio(cls, fio):
        if type (fio) != str:
            raise TypeError("FIO must be a string")
        
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Wronf value FIO")
        letters = ascii_letters + cls.ukrainian
        for char in f:
            if len (char.strip(letters)) != 0: 
                raise TypeError("FIO:only symbols, apostrophe and hyphen")
    
    @classmethod
    def validate_email(cls, email):
        if type (email) != str:
            raise TypeError("email must be a string")
        
        if '@' not in email:
            raise TypeError("Email must have @")
        f = email.split('@')
        local_part, domain_part = email.split('@', 1)
        
        if len(f) < 2:
            raise TypeError("email: Wronf value email (@)")
        firstpartemail = ascii_letters + digits + '.-_'
        for char in local_part:
            if len (char.strip(firstpartemail )) != 0: 
                raise TypeError("email: only symbols, digits and _-.")
            
        secondpartemail = ascii_letters + digits + '.-'
        for char in domain_part:
            if len (char.strip(secondpartemail)) != 0: 
                raise TypeError("email: only symbols, digits and _-.")

    def __str__(self):
        return f"{self.fio}, email: {self.email}, city: {self.__city}"

user1 = User("jhdsgjkjhkjh lkjglkjsljl ksdkgljlk", "jdfsjljjk@jkk.com","Kyiv")
print(user1)
try:
    user2 = User("John Smith", "sub.example.co.uk", "London")
except TypeError as e:
    print("Error:", e)
try:    
    user3 = User("Іван Петренко2 ehhhhkjkj", "ivan2@example!com", "Київ")
except TypeError as e:
    print("Error:", e)
try:    
    user4 = User(123, 5454554, "London")
except TypeError as e:
    print("Error:", e)
print("_________________EMAIL CHEKS_______________")

user5 = User("Кузьменко-Пилипчук Мар'яна Михайлівна", "jdfsjljjk@jkk.com","Kyiv")
print(user5)

user6 = User("FIO lkjglkjsljl ksdkgljlk", "jdfsjljjk@jkk.com","Kyiv")
print(user6)
try:
    user7 = User("FIO lkjglkjsljl ksdkgljlk", "sub.example.co.uk", "London")
except TypeError as e:
    print("Error:", e)
try:    
    user8 = User("Іван Петренко ehhhhkjkj", "ivan2@example!com", "Київ")
except TypeError as e:
    print("Error:", e)
try:    
    user9 = User("FIO lkjglkjsljl ksdkgljlk", 5454554, "London")
except TypeError as e:
    print("Error:", e)

user10 = User("Кузьменко-Пилипчук Мар'яна Михайлівна", "qwerty_uiuiu@sub.example.co.uk","Kyiv")
print(user10)

"""Task 2
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
You can refactor the existing code."""

#id_ - is just a random unique integer
print("-------------TASK 2------------")
class Boss:
    counter = 0
    def __init__(self, name: str, company: str):
        self.id = Boss.counter
        Boss.counter += 1
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers
    
    @workers.setter
    def workers (self, worker):
        self.validate_worker(worker)
        self._workers.append(worker)

    @workers.deleter
    def workers (self):
        del self._workers

    @classmethod
    def validate_worker(cls, worker):
        if not isinstance(worker, Worker):
            raise TypeError("Worker must be a worker class")
    
    def __str__(self):
        worker_names = ", ".join(w.name for w in self._workers) or "No workers"
        return f"Boss {self.name} ({self.company}) has workers: {worker_names}"

class Worker:
    counter =  0
    def __init__(self, name: str, company: str, boss: Boss):
        Worker.counter += 1
        self.id = Worker.counter
        self.name = name
        self.company = company
        if not isinstance(boss, Boss):
            raise TypeError("Boss must be a boss class")
        boss.workers = self

    @property
    def boss(self):
        return self._boss
    
    @boss.setter
    def boss (self, boss):
        self._boss = boss

    @boss.deleter
    def boss (self):
        del self._boss

boss1 = Boss("Mr. pister", "IT")
worker1 = Worker("Anna","IT", boss1)
worker2 = Worker("BOB","game", boss1)

boss2 = Boss("Mr. twister", "gambing")
worker3 = Worker("Lina", "gambing", boss2)
print(boss1)
print(boss2)
try:
    worker1 = Worker("Ann", "IT", "Petya")
except TypeError as e:
    print("Error:", e)

try:
    Boss.validate_worker("Ann")
except TypeError as e:
    print("Error:", e)

"""Task 3
Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):
methods:"""

"Don't forget to use @wraps"

from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to int")
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return str(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to string")
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to bool")
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except ValueError:
                raise ValueError(f"Cannot convert {result} to float")
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string
 

@TypeDecorators.to_bool
def do_something(string: str):
    return string
 
assert do_nothing('25') == 25
assert do_something('True') is True

print(do_nothing('25'))
print(type(do_nothing('25')))

print(do_something('True'))     # True
print(do_something('False'))    # False
print(type(do_something('True'))) # <class 'bool'>

# Перевірки через assert (автотести)
assert do_nothing('25') == 25
assert do_something('True') is True
try:
    assert do_something('False') is False
except AssertionError as e:
    print("Error:  assertation", e)