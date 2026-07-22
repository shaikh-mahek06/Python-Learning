def number():
    yield(10)
    yield(20)
    yield(30)

g=number()
print(next(g))
print(next(g))
print(next(g))

# Example 2: Generator with Loop
def count():
    for i in range(1,6):
        yield i
g=count()
print(next(g))
print(next(g))

# Example 3: Generator of Squares
def square():
    for i in range(1,6):
        yield i**2

g=square()
print(next(g))
print(next(g))
print(next(g))

# Example 4: Generator of Even Numbers
def even():
    for i in range(2,11,2):
        yield i
g=even()
print(next(g))
print(next(g))
print(next(g))

# Example 5: Generator of Characters
def letters():
    word = "Python"

    for ch in word:
        yield ch

g = letters()
print(next(g))
print(next(g))