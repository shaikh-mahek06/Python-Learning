# Question 1 – Write Your Name to a File
file=open("info.txt","w")
file.write("mahek shaikh")
file.close()

# 2.Store name, age, and city in a file.
file=open("info.txt","w")
file.write("Name : mahek shaikh\n")
file.write("Age : 21 \n")
file.write("City : Pune \n")
file.close()

# 3.Question 3 – Append New Data
file=open("info.txt","a")
file.write("Blood group : B+\n")
file.close()

# 4.Write the multiplication table of 5 into a file.
file=open("info.txt","a")

for i in range(1, 11):
    file.write(f"5 x {i} = {5 * i}\n")

file.close()


# Store a list of fruits.


fruits = [
    "Apple\n",
    "Banana\n",
    "Mango\n",
    "Orange\n"
]

file = open("info.txt", "a")

file.writelines(fruits)

file.close()

    
