import sys
# 1.Print the Python version.
print("1.Print the Python version.")
print(sys.version)

# 2.Print your operating system platform.
print("2.Print your operating system platform.")
print(sys.platform)

# 3.Print the path of the Python executable.
print("3.Print the path of the Python executable.")
print(sys.executable)

# 4.Print the list of module search paths
print("4.Print the list of module search paths")
print(sys.path)

# 5.Create a program that prints "Hello", calls sys.exit(), and then tries to print "World". Observe the output.
print("5.Create a program that prints 'Hello', calls sys.exit(), and then tries to print 'World' Observe the output.")

print("Hello")
sys.exit()
print("World")
