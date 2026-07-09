# 01
from itertools import *
c=count(1)
print(next(c))
print(next(c))
print(next(c))

# 02
color=cycle(["red","pink","white","green","black"])
print(next(color))
print(next(color))
print(next(color))
print(next(color))
print(next(color))
print(next(color))

# 03
for x in repeat("python",3):
    print(x)

# 04
nums=[1,2,3,4,5]

print(list(combinations(nums,2)))

# 05
print(list(permutations(nums,2)))

# 06
print(list(product(["a","b"],[1,2])))