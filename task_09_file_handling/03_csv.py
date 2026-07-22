import csv
file=open("students.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)

file.close()

# Print only student records (skip the header row).


import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)

# Count the total number of student records.
import csv

count = 0

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        count += 1

print("Total Students:", count)