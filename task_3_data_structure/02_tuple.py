
#1.	Create a tuple.
print("1.Create a tuple. ") 
my_tuple=(1,2,3,4,5,6,7,8,9,10,"a","b","c")
print(my_tuple)
#2.Single element tuple ((5,) vs (5)). 
print("2.ingle element tuple ((5,) vs (5)). ")
tup=(5)
tup2=(5,)
print(type(tup))
print(type(tup2))

#3.	Indexing. 
print("3.Indexing. ")
print(my_tuple[0:7])
#4.	Slicing. 
print("4.Slicing.")
slice=my_tuple[0:10]
print("slice of tuple is : ",slice)
#5.count() 
print("5.count() ")
print(slice.count(66))
#if it is element is not present in tuple return 0

#6.index()
print("6.index() ") 
print(my_tuple.index(6))
#if it is element is not present in tuple it cause error

#7.Packing & unpacking.
print("7.Packing & unpacking.")
tup3=("mango","apple","jamun","watermelon")
a,b,c,d= tup3
print("A : ",a)
print("B : ",b)
print("C : ",c)
print("D : ",d)
#8.Swap two variables using tuple unpacking.
print("8.Swap two variables using tuple unpacking. ") 
a,b=b,a
print("A : ",a)
print("B : ",b)

# 9.Tuple → List → Tuple conversion. 
print("9.Tuple → List → Tuple conversion")
print("tuple : ",type(tup3))
lst = list(tup3)
print("list : ",type(lst))

tup4=tuple(lst)
print("tuple : ",type(tup4))

# 10.	Reverse a tuple. 
print("10.Reverse a tuple. ")

print(tup3[::-1])

# 11.Find largest element. 
print(" 11.Find largest element. ")

largest=[0]
for word in tup3:
    if len(word)>len(largest):
        largest=word
print("largest element : ",largest)

# 12.Find smallest element. 
print(" 12.Find smallest element. ")
smallest=tup3[0]

for word in  tup3:
    if len(word) < len(smallest):
        smallest=word

print("smallest element : ",smallest)

# 13.Membership (in, not in). 
print(" 13.Membership (in, not in).")
print("orange" in tup3)
print("orange" not in tup3)

# 14.	Concatenate two tuples. 
print("14.Concatenate two tuples. ")
tup5=("mahek ")
tup6=("shaikh")
tup7=tup5+tup6
print(tup7)

#15. sum() use
tup8=(1,2,3,4,5)
print(sum(tup8))

# 16 Create a list of integers and sort it in ascending order.
print("16 Create a list of integers and sort it in ascending order.")
print(tuple(sorted((tup8))))

# 17.nested tuple
student = (
    ("Mahek", 21),
    ("Rahul", 22),
    ("Neha", 20)
)

print(student[0])
print(student[1][0])