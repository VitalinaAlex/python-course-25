
"""
Task 1
Write a program that reads in a sequence of characters and prints them in reverse order, using your implementation of Stack.
"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return self._items

    def pop(self):
        return self._items.pop()

    def reverse(self):
        reversed_string = ""
        string = self._items[:]
        if len(string)>0:
            for ch in string:
                self.push(ch)

            for ch in string:
                temp_char = self.pop()
                reversed_string += temp_char
            print(reversed_string)
        return
    def __str__(self):
        return str(self._items)

actions = Stack()
word = "qwerty"
for ch in word:
    actions.push(ch)
    print(actions)
actions.reverse()
