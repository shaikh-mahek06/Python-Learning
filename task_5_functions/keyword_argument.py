
#1. Call a function using keyword arguments. 
def info(name,age):
    print(name)
    print(age)

info(name="mahek",age=21)

# 2.Change the order of keyword arguments. 
info(age=21,name="mahek")

# 3.Mix positional and keyword arguments correctly. 
def greet(name,text="hie!!"):
    print(text , name)
    
greet(name="mahek")
