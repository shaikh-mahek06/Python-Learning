# 01
fruits = ["Apple", "Mango", "Banana"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

# Example 2: Starting Index from 1
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)

# Example 3: String
name = "Python"

for index, letter in enumerate(name):
    print(index, letter)

# Example 4: Tuple
numbers = (10, 20, 30)

for index, value in enumerate(numbers):
    print(index, value)

# Suppose you want to print a student attendance list.

students = ["Rahul", "Priya", "Amit"]

for roll_no, student in enumerate(students, start=101):
    print("Roll No:", roll_no, "Name:", student)