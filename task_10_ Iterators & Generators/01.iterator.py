# 01 List
numbers=[1,2,3,4,5,6,7,8,9,10]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 02 String
name="Mahek"
it=iter(name)
print(next(it))

# 03 tuple
data=(10,20,30)
it=iter(data)
print(next(it))
print(next(it))
print(next(it))

# 04  Dictionary
student = {
    "name":"Rahul",
    "age":21
}

it = iter(student)

print(next(it))
print(next(it))

data=(10,20,30)
it=iter(data)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("iteration completed")
        break
