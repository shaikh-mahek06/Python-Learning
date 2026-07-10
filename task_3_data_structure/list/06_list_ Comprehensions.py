# 9. Squares from 1 to 10/
squares=[i**2 for i  in range(1,11)]
print(squares)

# 10. Even numbers from 1 to 20
even=[i for i in range (1,21) if i%2==0]
print(even)

# 11. Convert all names to uppercase
color=["red","orange","pink","purple","pink"]
upper=[name.upper() for name in color]
print(upper)

# 12. Remove negative numbers
numbers = [10, -5, 7, -2, 15, -8]

positive = [i for i in numbers if i >= 0]

print(positive)

# 13. Find the second largest element
numbers = [10, 50, 20, 40, 30]

numbers = list(set(numbers))
numbers.sort()

print("Second Largest:", numbers[-2])

# 14. Remove duplicates while preserving order
numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print(result)