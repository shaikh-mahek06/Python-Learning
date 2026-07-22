# Example 1: Zip Two Lists
names = ["Amit", "Priya", "Rahul"]
marks = [85, 90, 78]

result = zip(names, marks)

# Example 2: Using a for Loop

print(list(result))
names = ["Amit", "Priya", "Rahul"]
marks = [85, 90, 78]
for name,mark in zip(names,marks):
    print(name,mark)

# Example 3: Zip Three Lists
names = ["Amit", "Priya", "Rahul"]
marks = [85, 90, 78]
city = ["Pune", "Mumbai", "Delhi"]

for n, m, c in zip(names, marks, city):
    print(n, m, c)

# Example 4: Zip Strings
word1 = "ABC"
word2 = "123"

for a, b in zip(word1, word2):
    print(a, b)

# Unzipping using zip()
students = [("Amit", 85), ("Priya", 90), ("Rahul", 78)]

names, marks = zip(*students)

print(names)
print(marks)