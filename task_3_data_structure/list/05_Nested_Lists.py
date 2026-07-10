# 6. Create a 3×3 matrix
matrix=[
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print(matrix)

# 7. Print the second column
for col in matrix:
    print(col[1])

# 8. Print the second row
print(matrix[1])

# 9. Find the sum of all elements
total=0
for row in matrix:
    for i in row:
        total += i
print(total)