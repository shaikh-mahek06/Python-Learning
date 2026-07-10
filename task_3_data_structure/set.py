# 1. Create a set of integers
print("# 1. Create a set of integers")
num ={1,2,3,4,5,6,7,6,5,4,5,78,}
print(num)

# 2. Add an element
print("# 2. Add an element")
num.add(99)
print(num)

# 3. Add multiple elements using update()
print("# 3. Add multiple elements using update()")
num.update([66,88,77,44])
print(num)

# 4. Remove an element using remove()
print("# 4. Remove an element using remove()")
num.remove(66)
print(num)   # cause error if element is not present

# 5. Remove an element using discard()
print("# 5. Remove an element using discard()")
num.discard(101)

# 6. Union of two sets
print("# 6. Union of two sets")
set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))

# 7. Intersection
print("# 7. Intersection")
print(set1.intersection(set2))

# 8. Difference
print("# 8. Difference")
print(set1.difference(set2))

# 9. Symmetric Difference
print("# 9. Symmetric Difference")
print(set1.symmetric_difference(set2))

# 10. Check if one set is a subset of another
print("# 10. Check if one set is a subset of another")
print(set1.issubset(set2))

# 11. Copy a set
print("# 11. Copy a set")
copy=set1.copy()
print(copy)

# 12. Clear a set
print("# 12. Clear a set")
copy.clear()
print(copy)

# 13. Pop one element
print("# 13. Pop one element")
new=set1.pop()
print(new)

# 14. Remove duplicates from a list
print("# 14. Remove duplicates from a list")
ls=[4,5,3,2,3,4,5,67,8,55,4,3,3,22,2]
result=list(set(ls))
print(result)

# 15. Count unique words
print("# 15. Count unique words")
text="life is full of blunders and life is stressfull too"
word=text.split()
unique_word=set(word)
print(unique_word)