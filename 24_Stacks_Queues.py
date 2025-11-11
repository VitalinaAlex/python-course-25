
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

"""
Task 2
Write a program that reads in a sequence of characters, and determines whether it's parentheses, braces, and curly brackets are "balanced."
🔹 План:
Створи стек.
Пройди по кожному символу рядка.
Якщо символ — відкрита дужка (, [, { — додай її у стек.
Якщо символ — закрита дужка, перевір чи остання у стеку відповідає їй:
Якщо так — pop()
Якщо ні — рядок не збалансований.
Наприкінці, якщо стек порожній → дужки збалансовані.
💡 Схожа вправа:
Перевір правильність дужок у математичному виразі "([5+3]*{2+4})".
"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return self._items

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        return str(self._items)

    def balanced(self):
        pairs = {')':'(', ']':'[', '}':'{'}
        temp_stack = Stack()
        # Ітеруємо по символах основного стеку (тобто по рядку, який в ньому зберігається)
        for ch in self._items:
            if ch in pairs.values():  # відкрита дужка
                temp_stack.push(ch)
            elif ch in pairs:         # закрита дужка
                if temp_stack.is_empty() or temp_stack.peek() != pairs[ch]:
                    return False
                temp_stack.pop()    # видаляємо відповідну відкриту дужку
        return temp_stack.is_empty()   # якщо стек порожній — дужки збалансовані

    def get_from_stack(self, e):
        temp = Stack()
        found = None
        
        while not self.is_empty():
            item = self.pop()
            if item != e:
                temp.push(item)
            else:
                found = item
        if found == None:
            raise ValueError("Value Error: found == None")
        print(temp)
        while not temp.is_empty():
            self.push(temp.pop())
        return found

balance = Stack()
example = "([5+3]*{2+4})"
for ch in example:
    balance.push(ch)
print(balance.balanced())

s1 = Stack()
for ch in "([{}])":
    s1.push(ch)
assert s1.balanced() == True, "Тест 1 не пройдено"

s2 = Stack()
for ch in "()[]{}":
    s2.push(ch)
assert s2.balanced() == True, "Тест 2 не пройдено"

s3 = Stack()
for ch in "([)]":
    s3.push(ch)
assert s3.balanced() == False, "Тест 3 не пройдено"

s4 = Stack()
for ch in "((())":
    s4.push(ch)
assert s4.balanced() == False, "Тест 4 не пройдено"

s5 = Stack()
assert s5.balanced() == True, "Тест 5 не пройдено"

s6 = Stack()
for ch in "if(x[0] == '{') { return true; }":
    s6.push(ch)
assert s6.balanced() == False, "Тест 6 не пройдено"

s6 = Stack()
for ch in "if(x[0] == '') { return true; }":
    s6.push(ch)
assert s6.balanced() == True, "Тест 7 не пройдено"
"""Task 3

Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. 
Any other element must remain on the stack respecting their order. Consider the case in which the element is not found - raise ValueError with proper info Message
"""

stack = Stack()
stack.push("Anna")
stack.push("Oleh")
stack.push("Marta")
print(stack)
print(stack.get_from_stack("Oleh"))
print(stack)

s7 = Stack()
for ch in ("Anna", "Annadg","Oleh", "Annaeirujgioe"):
    s7.push(ch)
print(s7)
assert s7.get_from_stack("Oleh") == "Oleh", "Тест 7 не пройдено"
print(s7)
assert str(s7) == "['Anna', 'Annadg', 'Annaeirujgioe']", "Тест 8 не пройдено"