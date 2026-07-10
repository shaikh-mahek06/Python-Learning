def info(**kwarg):
    print(kwarg)

info(name="mahek",age=21,blood_grp="b+")

# 2: Access a value
def student(**kwarg):
    print(kwarg["name"])
    print(kwarg["age"])

student(name="mahek",age=21,blood_grp="b+")

# 3: Print all details

def stud_info(**kwarg):
    for key,value in kwarg.items():
        print(key ,":", value)

stud_info(name="mahek",age=21,blood_grp="b+")

# 4: Employee Details
def employee(**kwarg):
    for key,value in kwarg.items():
        print(key ,":", value)

employee(name="alice",dept="IT",dept_id=167)

# 5: Count keyword arguments
def count(**kwarg):
    print(len(kwarg))

count(name="alice",dept="IT",dept_id=167)

