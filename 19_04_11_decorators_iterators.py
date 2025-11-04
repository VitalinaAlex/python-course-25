"""Task 1
Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters: 
'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function"""

def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

print("____Word____")
for index, value in with_index(["one", "two", "three"], start=1):
    print(index, value)

print("____Char____")
for index, ch in with_index("hello", start=0):
    print(index, ch)

print("____Tuple____")
for index, item in with_index((12, 2028, 32)):
    print(index, item)

print("____Dict____")
data = {"a": 8, "b": 5, "c": 12}
for index, key in with_index(data):
    print(index, key, " = ", data[key])

print("____set____")
for index, val in with_index({"x", "y", "z"}):
    print(index, val)

print("____not iterable____")
try:
    for index, value in with_index(1234):
        print(index, value)
except TypeError as e:
    print("Error:", e)

print("____nested____")
data = [[1, 2], [3, 4], [5, 6]]
for index, sublist in with_index(data):
    print(index, sublist)
"""Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters: 
'start', 'end', and optional step. Tips: See the documentation for 'range' function
"""

def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be 0")
    index = start
    if step > 0 and start < end:
        while index < end:
            yield index
            index += step
    elif step < 0 and start > end:
        while index > end:
            yield index
            index += step
    else:
        print(f"Something went wrong. check start, end, and step")

print(f"____Test____")
for i in in_range(1, 5):
    print("Step number", i)

print(f"____Test____")
for i in in_range(8, 5, -1):
    print("Step number", i)

print(f"____Test____")
for i in in_range(4, 8, -1):
    print("Step number", i)

print(f"____Test____")
for i in in_range(8, 8, -1):
    print("Step number", i)


print(f"____Test____")
try:
    for i in in_range(2, 5, 0):
        print("Step number", i)
except ValueError as e:
    print("Error:", e)

"""Task 3
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax."""


class MyIterable:
    def __init__(self, start, end, step = 1):
        if step == 0:
            raise ValueError("step cannot be 0")
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        index = self.start
        if self.step > 0:
            while index < self.end:
                yield index
                index += self.step
        else:
            while index > self.end:
                yield index
                index += self.step

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
    def __getitem__(self, index):
        value = self.start + index * self.step
        if (self.step > 0 and value >= self.end) or (self.step < 0 and value <= self.end):
            raise IndexError("index out of range")
        return value
    
    def __repr__(self):
        return f"InRange({self.start}, {self.end}, {self.step})"
    
r1 = MyIterable(1, 5)
print(r1[2])
print(list(r1))
print(r1)

r2 = MyIterable(8, 3, -2)
print(list(r2))
print(r2[1])
print(r2)