# Create:

#         Animal
#        /      \
#      Dog      Cat
#         \     /
#          Puppy

# Methods:

# eat()
# bark()
# meow()
# play()

# Create a Puppy object and call all four methods.

class animal():
    def eat(self):
        print("animals eats anything")
class dog(animal):
    def bark(self):
        print("they can bark ")
class cat(animal):
    def meow(self):
        print("they do meow meow!!!!")
class puppy(dog,cat):
    def play(self):
        print("they play woth humans")

d1=dog()
d1.eat()
d1.bark()
c1=cat()
c1.eat()
c1.meow()
p1=puppy()
p1.eat()
p1.bark()
p1.meow()
p1.play()
