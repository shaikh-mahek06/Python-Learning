# 1.•Square of a number. 
square=lambda x: x*x
print(square(7))

# 2.Cube of a number. 
cube=lambda x: x*x*x
print(cube(7))

# 3.Add two numbers. 
add=lambda x,y :x+y
print(add(7,3))

# 4: Even or Odd
even_odd=lambda n: "Even"if n%2==0 else "Odd"
print(even_odd(45753))

# 5: Largest Number
Largest=lambda a,b:a if a>b else b
print(Largest(7645678,8764776543))

# 7: String Length
lenght=lambda x : len(x)
print(lenght("Python"))

# 8: Reverse a String
rev=lambda x: x[::-1]
print(rev("Python"))

# 9: Lambda with sorted()
student=[
    ("alice",87),
    ("sara",97),
    ("jecob",84)
    
]
student=sorted(student, key=lambda x:x[1])
print(student)

# 10: Lambda with max()
student=max(student,key=lambda x:x[1])
print(student)



