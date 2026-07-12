# 1: Print all values
print("1: Print all values")
def func(*args):
    print(args)

func(7,6,5,4,3,6)

# 2: Print all values one by one
print("2: Print all values one by one")
def function(*args):
    for i in args:
        print(i)

function(0,9,8,7,6,"xyz")

# 3: Find the sum
print("3: Find the sum")
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

sum(6,7,8)

# 4: Find the largest number
print("4: Find the largest number")
def largest(*args):
    print(max(args))

largest(55,65,44)

# 5: Count how many arguments
def count_args(*args):
    print(len(args))
count_args(43,44,4,4)

# 6:Print all strings passed. 
print("6:Print all strings passed. ")
def print_strings(*args):
    for i in args:
        if isinstance(i,str):
            print(i)

print_strings("xyz","mahek",4,5,6)