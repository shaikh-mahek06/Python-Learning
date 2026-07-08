import calculator
calculator.calculator(2,2,"add")

#1.Import only the sqrt() function from the math module and find the square root of a number.
print("1.Import only the sqrt() function from the math module and find the square root of a number.")
from math import sqrt
print("sqrt of 81 : ",sqrt(81))

# 2.Import only the factorial() function and find the factorial of a number.
print("2.Import only the factorial() function and find the factorial of a number.")
from math import factorial
print("Factorial of 6 : ",factorial(6))

#3.Import the math module and print the value of π.
print("3.Import the math module and print the value of π.")
from math import pi
print("value of pi : ",pi)
 
#  4.Import multiple functions (sqrt, pow, factorial) using a single from...import statement.
print("4.Import multiple functions (sqrt, pow, factorial) using a single from...import statement.")

from math import pow ,factorial, sqrt,e
print("value of e : ",e)
print("5th power of 3 : ",pow(3,5))
print("Factorial of 6 : ",factorial(6))

#5.Find the cube of a number using pow().
print("5.Find the cube of a number using pow().")
print("cube of 4 : ",pow(4,3))
import math
# 6.Find the ceiling and floor of a decimal number.
print("6.Find the ceiling and floor of a decimal number.")
print("ceiling : ",math.ceil(3.33))
print("floor : ",math.floor(5.66))

# 7.Find the GCD and LCM of two numbers
print("7.Find the GCD of two numbers")
num1=67
num2=88
print("GCD is : ",math.gcd(num1,num2))
print("LCM is : ",math.lcm(num1,num2))
# 8.degree to radians
print("8.degree to radians")
print(math.radians(90))

"""9. Find the value of:
sin(30°)
cos(60°)
tan()45°"""

print("sin(30°) : ",math.sin(math.radians(30)))
print("cos(30°) : ",math.cos(math.radians(30)))
print("tan(30°) : ",math.tan(math.radians(45)))

colors=["pink","red","orange","white"]


