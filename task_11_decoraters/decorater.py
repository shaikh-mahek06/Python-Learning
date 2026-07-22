# 1 . Using @ Decorator Syntax
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def hello():
    print("Hello World")


hello()

# 2 . Decorator with Arguments
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Addition Starts")

        result = func(*args, **kwargs)

        print("Addition Ends")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(5, 10))

# 3. Decorator Returning Values
def decorator(func):

    def wrapper():
        print("Calculating...")

        return func()

    return wrapper


@decorator
def number():
    return 100


print(number())

# 4. Multiple Decorators

def star(func):
    def wrapper():
        print("*"*20)
        func()
        print("*"*20)
    return wrapper
def hash(func):
    def wrapper():
        print("#"*20)
        func()
        print("#"*20)
    return wrapper
@star
@hash
def message():
    print("      Mahek")


message()

# 5
def login_required(func):

    def wrapper():
        logged_in = False

        if logged_in:
            func()
        else:
            print("Please Login")

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()

# 6 Real Life Example – Execution Time
import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


@timer
def work():

    for i in range(1000000):
        pass


work()