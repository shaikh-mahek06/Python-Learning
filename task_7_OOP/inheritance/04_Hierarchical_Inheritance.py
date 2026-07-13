# Question 1 

# Create

# Animal
#  /   \
# Dog  Cat

# Methods:
# eat()
# bark()
# meow()

class animal():
    def eat(self):
        print("they eat other animals")
class dog(animal):
    def bark(self):
        print("dogs can bark-BHAU BHAU")

class cat(animal):
    def meow(self):
        print("cats do meow -meow")

c1=cat()
c1.eat()
c1.meow()
d1=dog()
d1.eat()
d1.bark()

# Question 4 ⭐⭐

# Create

# Shape
#  /      \
# Circle Rectangle

# Methods:

# draw()
# area_circle()
# area_rectangle()

import math
class shape():
    def draw(self):
        print("draw a shape")

class circle(shape):
    def area_circle(self,radius):
        print(math.pi*radius**2)

class rectangle(shape):
    def rect_area(self,l,b):
        print(2*l*b)

cr1=circle()
cr1.draw()
cr1.area_circle(3)
r1=rectangle()
r1.draw()
r1.rect_area(3,3)