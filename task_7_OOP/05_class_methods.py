# 25. Student Class

# Maintain total students using class variable.
# Create a class method
# display_total_students()

class student():
    total=0
    def __init__(self):
        student.total+=1

    @classmethod
    def display_total_students(cls):
        print(cls.total)


student()
student()

student.display_total_students()

# 26. Employee Class

# Class variable

# company_name

# Create class method

# change_company(new_name)

# All employees should reflect updated company.

class Employee:
    company_name = "TCS"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name


Employee.change_company("Infosys")

print(Employee.company_name)

"""27. Bank Class

Class variable

bank_name

Create class method

change_bank_name()

Display updated bank name."""

class Bank:
    bank_name = "SBI"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


Bank.change_bank_name("HDFC")

print(Bank.bank_name)
