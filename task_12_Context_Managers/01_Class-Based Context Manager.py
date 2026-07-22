class MyContext():
    def __enter__(self):
        print("Enterd context")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Exit context")
with MyContext():
    print("Inside the block")

# Example 2: File Handling
class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File Closed")


with FileManager("sample.txt", "w") as f:
    f.write("Hello Python")

# Example 3: Exception Handling
class Demo:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception Type:", exc_type)
        print("Cleanup Done")
        return True      


with Demo():
    print(10 / 0)

print("Program Continues")
# Example 4: Timer
import time

class Timer:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print("Execution Time:", end - self.start)


with Timer():
    time.sleep(2)