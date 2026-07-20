# 1.Read all lines and print the returned list.
print("1.Read all lines and print the returned list.")
file=open("py_notes.txt","r")
print(file.readlines())
file.close()

# Question 2 – Read First Line
print("Question 2 – Read First Line")
file=open("py_notes.txt","r")
print(file.readline())
file.close()

# Question 3 – Read Entire File
print("Question 3 – Read Entire File")
file=open("py_notes.txt","r")
print(file.read())
file.close()

# Question 4 – Count Number of Lines
print("Question 4 – Count Number of Lines")
file=open("py_notes.txt")
count=0
for line in file:
    count+=1
print ("Total lines : ",count)
file.close()

# Question 5 – Count Number of Words
print("Question 5 – Count Number of Words")
file=open("py_notes.txt")
content=file.read()
word=content.split()
print("total words : ",len(word))