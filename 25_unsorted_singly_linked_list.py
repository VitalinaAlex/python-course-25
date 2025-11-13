"""Task 1. Extend UnsortedList
Implement append, index, pop, insert methods for UnsortedList. 
Also implement a slice method, which will take two parameters 'start' and 'stop', 
and return a copy of the list starting at the position and going up to but not including the stop position."""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    def __init__(self):
        self.head = None

    def append(self, item):
        new = Node(item)
        if not self.head:
            self.head = new
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new

    def index(self, item):
        current = self.head
        position = 0
        while current:
            if current.data == item:
                return position
            current = current.next
            position += 1
        raise ValueError(f"{item} is not in list")

    def pop(self, pos):
        if pos < 0:
            raise IndexError("pop index out of range")
        current = self.head
        if pos == 0:
            if not current:
                raise IndexError("pop from empty list")
            self.head = current.next
            return current.data
        prev = None
        for p in range(pos):
            prev = current
            if not current:
                raise IndexError("pop index out of range")
            current = current.next
        if not current:
            raise IndexError("pop index out of range")
        prev.next = current.next
        return current.data

    def insert(self, pos, item):
        new = Node(item)
        if pos <= 0 or not self.head:
            new.next = self.head # новий вузол вказує на стару голову
            self.head = new # голова тепер новий вузол
            return
        current = self.head
        prev = None
        count = 0
        while current and count < pos:
            prev = current
            current = current.next
            count += 1

        new.next = current
        if prev:
            prev.next = new

    def slice(self, start, stop):
        new_list = UnsortedList()
        current = self.head
        position = 0
        while current and position < stop:
            if position >= start:
                new_list.append(current.data)
            current = current.next
            position += 1
        return new_list
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"

n=5
my_list = UnsortedList()
for i in range(n):
    my_list.append((i+1)*n)
print(my_list)
assert str(my_list) == "[5, 10, 15, 20, 25]"

result1 = my_list.slice(1, 4)
print(result1)
assert str(result1) == "[10, 15, 20]"

my_list.insert(0, 0)
print(my_list)
assert str(my_list) == "[0, 5, 10, 15, 20, 25]"

my_list.insert(7, 35)  # вставка в кінець
print(my_list)
assert str(my_list) == "[0, 5, 10, 15, 20, 25, 35]"

my_list.insert(4, 22)  # середина
print(my_list)
assert str(my_list) == "[0, 5, 10, 15, 22, 20, 25, 35]"

pop1 = my_list.pop(4)  # видалення з позиції 4
print(f"Popped: {pop1}")
assert pop1 == 22
print(my_list)
assert str(my_list) == "[0, 5, 10, 15, 20, 25, 35]"

pop2 = my_list.pop(0)  # видалення з початку
print(f"Popped: {pop2}")
assert pop2 == 0
print(my_list)
assert str(my_list) == "[5, 10, 15, 20, 25, 35]"

index_of_15 = my_list.index(15)
print(f"Index of 15: {index_of_15}")
assert index_of_15 == 2

# Тестування з рядками
my_string_list = UnsortedList()
for char in "hello":
    my_string_list.append(char)
print(my_string_list)
assert str(my_string_list) == "['h', 'e', 'l', 'l', 'o']"

result = my_string_list.slice(1, 4)
print(result)
assert str(result) == "['e', 'l', 'l']"

index_of_l = my_string_list.index('l')
print(f"Index of 'l': {index_of_l}")
assert index_of_l == 2

pop3 = my_string_list.pop(3)
print(f"Popped: {pop3}")
assert pop3 == 'l'
print(my_string_list)
assert str(my_string_list) == "['h', 'e', 'l', 'o']"

"""
🧩 Task 2. Stack using Linked List
🔹 План:
Використати клас Node (той самий).
Створити клас Stack з атрибутом head.
push(item) — додати елемент на початок (O(1)).
pop() — видалити елемент з початку (O(1)).
peek() — подивитись верхівку (O(1)).
is_empty() — перевірити, чи стек порожній.
💡 Тут зручно використовувати лише “голову” (head), без хвоста.

"""
class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new = Node(item)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            raise IndexError("pop from empty stack")
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if not self.head:
            raise IndexError("peek from empty stack")
        return self.head.data

    def is_empty(self):
        return self.head is None
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "Stack top -> [" + ", ".join(elements) + "]"
    
my_stack = Stack()
for i in range(n):
    my_stack.push((i+1)*10)
print("Stack after pushes:")
print(my_stack)
assert str(my_stack) == "Stack top -> [50, 40, 30, 20, 10]"

top_item = my_stack.peek()
print(f"Top item (peek): {top_item}")
assert top_item == 50
popped_item = my_stack.pop()
print(f"Popped item: {popped_item}")
assert popped_item == 50
print("Stack after pop:")
print(my_stack)
assert str(my_stack) == "Stack top -> [40, 30, 20, 10]"
is_empty = my_stack.is_empty()
print(f"Is stack empty? {is_empty}")
assert is_empty == False

"""🧩 Task 3. Queue using Linked List
🔹 План:
Знову використовуємо Node.
Клас Queue має два вказівники:
head — початок черги (звідси видаляємо),
tail — кінець черги (сюди додаємо).
enqueue(item) — додати в кінець.
dequeue() — видалити з початку.
peek() — подивитись перший елемент.
is_empty() — перевірити, чи черга порожня.
"""
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new = Node(item)
        if not self.tail:
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            raise IndexError("dequeue from empty queue")
        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return item

    def peek(self):
        if not self.head:
            raise IndexError("peek from empty queue")
        return self.head.data

    def is_empty(self):
        return self.head is None
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.data))
            current = current.next
        return "Queue front -> [" + ", ".join(elements) + "] <- rear"   
    
my_queue = Queue()
for i in range(n):
    my_queue.enqueue((i+1)*10)
print("Queue after enqueues:")
print(my_queue)
assert str(my_queue) == "Queue front -> [10, 20, 30, 40, 50] <- rear"
front_item = my_queue.peek()
print(f"Front item (peek): {front_item}")
assert front_item == 10
dequeued_item = my_queue.dequeue()
print(f"Dequeued item: {dequeued_item}")
assert dequeued_item == 10
print("Queue after dequeue:")
print(my_queue)
assert str(my_queue) == "Queue front -> [20, 30, 40, 50] <- rear"
is_empty = my_queue.is_empty()
print(f"Is queue empty? {is_empty}")
assert is_empty == False    