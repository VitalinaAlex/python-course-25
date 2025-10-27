"""Task 1
A Person class
Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. 
Make another method called talk() which makes prints a greeting from the person containing, for example like this: "Hello, my name is Carl Johnson and I’m 26 years old"."""
import inspect

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        result = (f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old!")
        print(result)

my_friend = Person ("Olga", "Golubovska",34)
my_friend.talk()
famous_writer = Person("Steven","King", 98)
famous_writer.talk()
print (f"{famous_writer.firstname} {famous_writer.lastname} - Famous writer")
"""Task 2
Doggy age
Create a class Dog with class attribute 'age_factor' equals to 7. Make __init__() which takes values for a dog’s age. 
Then create a method `human_age` which returns the dog’s age in human equivalent."""
class Dog:
    age_factor = 7
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_age(self):
        print(f"{self.name} has {self.age * Dog.age_factor} y.o")
my_dog = Dog ("Charly",5)
my_dog.human_age()
"""Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:"""
"""
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", 
if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above."""
class TVController:
    current_index = 0
    def __init__(self, channels):
        self.current_index = 0
        self.channels = channels

    def first_channel(self):
        print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")

    def turn_channel(self, N):
        if N <= len(self.channels) and N>=0:
            self.current_index = N - 1
            print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")

    def current_channel(self):
        print(f"{inspect.currentframe().f_code.co_name} {self.current_index + 1} - {self.channels[self.current_index]}")
        return self.channels[self.current_index]
    def exists(self, arg):
        if isinstance(arg, int):
            if 1 <= arg <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif isinstance(arg, str):
            if arg in self.channels:
                return "Yes"
            else:
                return "No"

CHANNELS = ["BBC", "Discovery", "TV1000","1+1", "ICTV", "NTN"]

controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
print(controller.exists(7)) == "No"
print(controller.exists("BBC")) == "Yes"
print(controller.exists(4)) == "Yes"
print(controller.exists("TNT")) == "No"