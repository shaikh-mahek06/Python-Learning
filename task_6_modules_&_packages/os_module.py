import os
# 1.current working directory
print("1.current working directory")
print(os.getcwd())

# 2.Lists all files and folders in the current directory.
print("2.Lists all files and folders in the current directory.")
print(os.listdir())

# 3.Create a folder named Practice.
print(" 3.Create a folder named Practice.")
print(os.mkdir("Practice"))

# 4.Rename Practice to PythonPractice.
print("4.Rename Practice to Rename Practice to PythonPractice..")
print(os.rename("Practice","PythonPractice"))
# 5.create file
print(os.mkdir("PythonPractice.txt"))

# 7 os name
print(os.name)

# 8 Check if a file/folder exists
print(" 8 Check if a file/folder exists")
print(os.path.exists("Practice"))
#9. Join paths
path = os.path.join("Practice", "PythonPractice.txt")
print(path)