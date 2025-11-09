"""Task 1
File Context Manager class
Create your own class, which can behave like a built-in function 'open'. 
Also, you need to extend its functionality with counter and logging. 
Pay special attention to the implementation of '__exit__' method, 
which has to cover all the requirements to context managers mentioned here:"""
from functools import wraps

# ANSI-коди кольорів для консолі
GRAY = "\033[32m"
RESET = "\033[0m"

def log_test(func):
    """Декоратор для логування юніт тесту."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        test_name = self._testMethodName
        print(f"\n{GRAY}--- START {test_name} ---{RESET}")
        try:
            result = func(self, *args, **kwargs)
            print(f"\n{GRAY}--- END {test_name} ---{RESET}")
            return result
        except Exception as e:
            print(f"\n{GRAY}--- ERROR in {test_name}: {e} ---{RESET}")
            raise
    return wrapper

class FileOpen:
    counter = 0  # загальний лічильник відкриттів
    print("FileOpen class")

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        FileOpen.counter += 1
        self.file = open(self.filename, self.mode)
        print(f"[DEBUG log] Opened {self.filename} (Attempt: {FileOpen.counter})")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"[DEBUG log] Closed {self.filename}")
        
        if exc_type:
            print(f"[DEBUG log] {exc_type.__name__}: {exc_val}")
        return False
file = "file.txt"
with FileOpen(file, "w") as f:
    f.write("Hello!")

with FileOpen(file, "a") as f:
    f.write("By!")

with FileOpen(file, "a") as f:
    f.write("By-by!")

with FileOpen(file, "r") as f:
    print(f.read())

"""Task 2
Writing tests for context manager
Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
And also, write tests when your class raises errors or you have errors in the runtime context suite."""

import unittest

class TestFileOpen(unittest.TestCase):
    print("-----------TestFileOpen class-----------")
    @log_test
    def test_write_and_read(self):
        # створюємо і записуємо
        with FileOpen(file, "w") as f:
            f.write("Hello, world!")

        # читаємо
        with FileOpen(file, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello, world!")
    
    @log_test
    def test_counter(self):
        start = FileOpen.counter
        with FileOpen(file, "w"):
            return
        self.assertEqual(FileOpen.counter, start + 1)

    @log_test
    def test_file_not_found(self):
        print("[DEBUG log] file not found")
        with self.assertRaises(FileNotFoundError):
            with FileOpen("file_.txt", "r"):
                return

if __name__ == "__main__":
    unittest.main()

