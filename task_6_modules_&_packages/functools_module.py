
from functools import *

# 01
print("# 01")
number=[5,2,3]
result=reduce(lambda x,y: x+y,number)
print(result)

# 02
print("# 02")
print(reduce(lambda x,y : x*y,number))

# 03
def power(base,exponent):
    return base**exponent

square=power(3,exponent=2)
print(square)

# 04
cube=power(4,exponent=3)
print(cube)

# 05
from functools import lru_cache

@lru_cache(maxsize=None)
def square(n):
    print("Calculating...")
    return n*n

print(square(5))
print(square(5))
print(square(6))