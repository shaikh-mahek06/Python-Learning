# 1. Create a dictionary of a student (name, age, city)
student={
    "name":"mahek",
    "age":21,
    "city":"pune"
}
print(student)

# 2. Print the value of "name"
print(student["name"])

# 3. Add a new key "course"
student["course"]="AIML"
print(student)

# 4. Update the "age"
student["age"]=22
print(student["age"])

# 5. Delete "city"
del student["city"]
print(student)

# 6. Check whether "age" exists
if "age" in student:
    print("is exists")
else:
    print("not exists")

# 7. Print all keys
print(student.keys())

# 8. Print all values
print(student.values())

# 9. Print all key-value pairs
print(student.items())

# 10. Use get() to access a key
print(student.get("name"))

# 11. Make a copy of the dictionary
new=student.copy()
print(new)

# 12. Clear the dictionary
new.clear()
print(new)

# 16. Create a nested dictionary
info={
    "stud_1":{
        "personal":{
            "name":"sara",
            "age":27
        },
        "marks":{"SQL":87,
               "python":88

        }
    },
    "stud_2":{
        "personal":{
            "name":"alice",
            "age":25
        },
        "marks":{"SQL":77,
               "python":83

        }
    }
}
print(info)

# 17. Print "Python" marks from the nested dictionary

print(info["stud_1"]["marks"]["python"])

# 18. Create a dictionary of numbers and their squares
square = {num : num**2 for num in range(1, 6)}

print(square)

# 19. Create a dictionary containing even numbers from 1 to 10 and their cubes
cube = {num: num**3 for num in range(1, 11) if num % 2 == 0}

print(cube)