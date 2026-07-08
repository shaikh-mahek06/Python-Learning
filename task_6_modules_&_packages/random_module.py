import random
# 1.Generate a random number between 1 and 100.
print("Generate a random number between 1 and 100.")
print(random.randint(1, 100))

#2.Generate a random floating-point number.
print("2.Generate a random floating-point number.")
print(random.random())

print(random.uniform(10,12))
# 4.select random color
print("4.select random color")
color=["pink","red","white","orange"]
print(random.choice(color))

# 5.select 2 random color
print(" 5.select 2 random color")
print(random.choices(color,k=2))

#  6.select random char from string
name="mahek shaikh"
print(random.choice(name))
# 7 sample
list=[1,2,2,3,4,5,5,4,6,7,66,6,5,9,4,44,]
print(random.sample(list,k=1))
# 8.shuffle the list
print(" 8.shuffle the list")
random.shuffle(list)
print(list)

# 9.random seed
random.seed(5)
print(random.randint(1,100))
