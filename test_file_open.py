from functools import wraps
import pytest
from file_open import FileOpen
# ANSI-коди кольорів для консолі
GRAY = "\033[32m"
RESET = "\033[0m"

def log_test(func):
    """Декоратор для логування pytest-тесту."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        test_name = func.__name__
        print(f"\n{GRAY}--- START {test_name} ---{RESET}")
        try:
            result = func(*args, **kwargs)
            print(f"{GRAY}--- END {test_name} ---{RESET}")
            return result
        except Exception as e:
            print(f"{GRAY}--- ERROR in {test_name}: {e} ---{RESET}")
            raise
    return wrapper

@log_test
def test_write_and_read():
    # створюємо і записуємо
    with FileOpen("test.txt", "w") as f:
        f.write("Hello, world!")

    # читаємо
    with FileOpen("test.txt", "r") as f:
        content = f.read()
    assert content == "Hello, world!"
    
@log_test
def test_counter():
    start = FileOpen.counter
    with FileOpen("test.txt", "w"):
        pass
    assert FileOpen.counter == start + 1

@log_test
def test_file_not_found():
    print("[DEBUG log] file not found")
    with pytest.raises(FileNotFoundError):
        with FileOpen("file_.txt", "r"):
            pass
#pytest -s -v для запуска