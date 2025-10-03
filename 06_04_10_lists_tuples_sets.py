"""Task 1
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers"""
import random
listofnumbers=[]
length=10
element=0
max=0
while element < length:
    listofnumbers.append(random.randint(1,1000))
    print(f"Add element {listofnumbers[element]} with index{element}")
    if max < listofnumbers[element]:
        max = listofnumbers[element]
        print(f'Max = {max}')
    element += 1
print(listofnumbers)
print(f'Max = {max}')
print(f'List length = {len(listofnumbers)}')

"""Task 2
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers"""
import random
listfirst=[]
listsecond=[]
length=10
element=0
while element < length:
    listfirst.append(random.randint(1,10))
    listsecond.append(random.randint(1,10))
    element += 1
setfirst = set(listfirst)
setsecond = set(listsecond)
print(setfirst)
print(setsecond)
print(setfirst.intersection(setsecond))

"""Task 3
Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration"""
lista = []
listb = []
length = 100
element = 1
while element <= length:
    lista.append(element)
    if element % 7 == 0 and element % 5 != 0:
        listb.append(element)
    element += 1
print('List A: ',lista)
print('List B: ',listb)
print(f'Length of list A = {len(lista)},length of list B = {len(listb)}')
