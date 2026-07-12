# 21. Math Utility

# Create static methods

# square()
# cube()
class math_utility():
    @staticmethod
    def square(x):
        print("square : ",x*x)
    @staticmethod
    def cube(x):
        print("cube : ",x**3)

math_utility.square(8)
math_utility.cube(8)

# 22. Age Checker
# Static method
# check_age(age)
# Returns whether eligible for voting.

class AgeChecker():

    @staticmethod
    def check_age(age):
        return age >= 18


print(AgeChecker.check_age(20))

# 23. Number Utility

# Static methods

# even_or_odd()
# prime()
# palindrome()

class NumberUtility:

    @staticmethod
    def even_or_odd(n):
        return "Even" if n % 2 == 0 else "Odd"

    @staticmethod
    def prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def palindrome(n):
        return str(n) == str(n)[::-1]


print(NumberUtility.even_or_odd(10))
print(NumberUtility.prime(7))
print(NumberUtility.palindrome(121))
    

# 24. Temperature Utility

# Static methods

# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Kelvin to Celsius

class TemperatureUtility:

    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5 / 9

    @staticmethod
    def k_to_c(k):
        return k - 273.15
    
print(TemperatureUtility.k_to_c(699))