# Question 1 ⭐

# Create a Father class with a method drive().

# Create a Mother class with a method cook().

# Create a Child class that inherits from both.

# Call both methods.

class father():
    def drive(self):
        print("father know how to drive")
class mother():
    def cook(self):
        print("mother knows how to cook")

class child(father,mother):
    pass

c1=child()
c1.drive()
c1.cook()

# Question 2 ⭐

# Create a Camera class with a method click().

# Create a Phone class with a method call().

# Create a SmartPhone class that inherits from both.

class camera():
    def click(self):
        print("camera clicks a picture")

class phone():
    def call(self):
        print("phone makes a call")

class smartphone(camera,phone):
    pass

p1=smartphone()
p1.click()
p1.click()

# Question 3 

# Create a Teacher class with a method teach().

# Create a Singer class with a method sing().

# Create a MusicTeacher class that inherits from both.

class teacher():
    def teach(self):
        print("teacher teaches a subject")

class singer():
    def sing(self):
        print("singer sings a song")

class music_teacher(teacher,singer):
    pass

m1=music_teacher()
m1.teach()
m1.sing()

# Question 4 ⭐⭐

# Create an Employee class with a method work().

# Create a Person class with a method display().

# Create a Manager class that inherits from both.

class employee():
    def work(self):
        print("they work!!")
class person():
    def display(self):
        print("display anything")

class manager(employee,person):
    pass

x1=manager()
x1.work()
x1.display()

# Question 5 ⭐⭐⭐ (Most Important)

# Create two parent classes.

# Both should have a method named: show
class male():
    def show(self):
        print("he is male")
class female():
    def show(self):
        print("she is female")

class human(male,female):
    pass

h1=human()
h1.show()
h1.show()