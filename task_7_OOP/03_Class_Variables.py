# 16. Employee Counter

class employee():
    total=0

    def __init__(self):
        employee.total+=1

e1=employee()
e2=employee()
e3=employee()
e4=employee()
print(employee.total)

# 17. Student Counter
class student():
    total=0
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        student.total+=1
s1=student("Emma","CS")
s2=student("Alice","AIML")
print(student.total)

# 18. Car Showroom

# Class variable : showroom_name
# Instance variables : model,brand
# Display showroom and car details.

class car():
    showroom_name="XYZ"
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    
    def display(self):
        print(car.showroom_name,self.model,self.brand)

c1=car("Innova","Toyota")
c1.display()

# 19. School Class
# Class variable : school_name
# Allow changing school name for every student using class variable.
        
class school():
    school_name="KV school"

    def __init__(self,name):
        self.name=name

s1=school("Emma")
print(school.school_name)
school.school_name="ABC"
print(school.school_name)

# 20. Product Class
# Class variable : GST = 18%
# Calculate final price after GST.       

class product():
    GST=18
    def __init__(self,price):
        self.price=price

    def price_with_gst(self):
        total_price=self.price * product.GST /100
        print(total_price)
        
p1=product(7000)
p1.price_with_gst()

    