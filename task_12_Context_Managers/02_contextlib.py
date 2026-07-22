# Example 1: Basic Example
from contextlib import contextmanager

@contextmanager
def demo():
    print("Enter")
    yield
    print("Exit")


with demo():
    print("Inside Block")

    # Example 2: File Handling
from contextlib import contextmanager

@contextmanager
def open_file(name, mode):

    file = open(name, mode)

    yield file

    file.close()
    print("File Closed")


with open_file("sample.txt", "w") as f:
    f.write("Hello")

# Example 3: Timer
from contextlib import contextmanager
import time

@contextmanager
def timer():

    start = time.time()

    yield

    end = time.time()

    print("Execution Time:", end - start)


with timer():
    time.sleep(3)