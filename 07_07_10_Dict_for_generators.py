"""Task 1
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. """

string = input('Enter a sentence...')
words = string.split()
setwithwords = set(words)
print('Рядок :',string)
print('Множина :',setwithwords)
count=0
dictionary = dict()
for word in setwithwords:
    count = string.count(word)
    dictionary[word] = count
print(dictionary)

"""Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
The code has to return the dictionary with the sums of the prices by the goods types."""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
totalprice = dict()
for key in stock:
    totalprice[key] = stock[key]*prices[key]
print('Price ', prices)
print('Stock ', stock)
print('Total ', totalprice )

"""Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared."""
alist = []
atuple = ()
for i in range(1, 11):
    atuple = (i, i**2)
    alist.append(atuple)
print(alist) 

"""Task 4
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,"""
import calendar
week = dict()
reverseweek = dict()
reverse = dict()
for i in range(1, 8):
    week[i] = calendar.day_name[i-1]
    reverseweek[calendar.day_name[7-i]] = 8-i
    reverse[calendar.day_name[i-1]] = i
print(week)
for key, value in week.items():
    print(key, " → ", value)
print(reverseweek)
for key, value in reverseweek.items():
    print(key, " → ", value)
print(reverse)
for key, value in reverse.items():
    print(key, " → ", value)
