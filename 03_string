# 1.Strings slicing
print("1.Strings slicing")
# 1.Store "Python" in a variable and print: First character Last character
print("1.Store 'Python' in a variable and print: First character Last character")


string1=  'Python'
print(string1)
print("First character", string1[0])
print("last character", string1[-1])

# 2.Print the first 6 characters.
print("2.Print the first 6 characters.")
text = "PythonProgramming"
print(text[0:7])

# 3.Print only: Programming
print("3.Print only: Programming")
print(text[6:])

# 4.Print every second character.
print(len(text))
print(text[0 : :2])

#Print every 3rd character 
print("Print every 3rd character")
print(text[ : : 3])
# 4.Reverse the string using slicing.

print("4.Reverse the string using slicing.")
print(text[ : :-1])
# 2. Modify Strings
print("2. Modify Strings")

# 1.Convert the following string into uppercase.
print("1.Convert the following string into uppercase.")
print(text.upper())

# 2.Convert the following string into lowercase.
print("2.Convert the following string into lowercase.")
print(text.lower())

# 3.Remove extra spaces.
print("3.Remove extra spaces.")
word="   mahek " 
print(word.strip(" "))
print(word.lstrip(" "))
print(word.rstrip(" "))

# 4.Replace "Java" with "Python".
print("4.Replace Java with Python.")
text1 = "I love Java"
print(text1.replace("Java","Python"))

# 3.Concatenate Strings 
print("3.Concatenate Strings ")

# 1.Join two strings.
print("1.Join two strings.")

a = "Hello "
b = "World"
print(a + b)

# 4. Format Strings
print("4. Format Strings")

name = "Mahek"
age = 21
print(f"my name is {name} and age is {age}")
print(string1.title())

#1.Reverse a string
print("1.Reverse a string")

print(string1[ : :-1])

#2.Palindrome
print("2.Palindrome")
word1="madam"
print("word is: ",word1)

if word1[ : ]==word1[ : :-1]:
    print("it is Palindrome ")
else:
    print("it is not Palindrome")

#4.Check if a string contains only alphabets
print("4.Check if a string contains only alphabets")
print(word1.isalpha())

# 5.Count vowels
print("5.Count vowels")
count=0
vowels="aeiouAEIOU"
for ch in text1:
    if ch in vowels:
        count +=1

print(count)

# 6.Count character frequency
print("6.Count character frequency")
frequency={}
for ch in text1:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1

print(frequency)
#7.frequency of spaces
freq=0
for ch in text1:
    if ch==" ":
        freq+=1
    
print(freq)

#8.Check anagram
print("8.Check anagram")
wrd1="listen"
wrd2="listen"
w1={}
for ch in wrd1:
    if ch in w1:
        w1[ch]+=1
    else:
        w1[ch]=1

w2={}

for ch in wrd2:
    if ch in w2:
        w2[ch]+=1
    else:
        w2[ch]=1

print("w1:",w1)
print("w2:",w2)

if w1==w2:
    print("is anagram")
else:
    ("no anagram")

#9.Count consonants
print("9.Count consonants")
vowel="aeiouAEIOU"
count=0
for ch in text:
    if ch != vowel:
        count +=1
    else:
        count=1

print ("consonants are : ",count)

    
#10.Reverse words in a sentence
print("10.Reverse words in a sentence")

sentence="coding is complicated"
print("normal string : ",sentence)
split=sentence.split()
reverse=split[ : :-1]
join=" ".join(split)
print("Reverse string is : ", join)

#11.Longest word in a sentence 
print("11.Longest word in a sentence ")
longest=split[0]
for i in split :
    if len(i)>len(longest):
        longest=i
    
print("Longest word is:", longest)


# 12.Shortest word in a sentence 
print("12.Shortest word in a sentence ")

Shortest=split[0]
for i in split:
    if len(split)<len(Shortest):
        Shortest=i

print("Shortest word is:", Shortest)

#14.Replace multiple spaces with one space 
sent="  mahek      javed      shaikh   "
x=sent.split()
y=" ".join(x)
print(y)

#15. String Compression
print("15.String Compression")

text = input("Enter a string: ")

count = 1
result = ""

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1
result += text[-1] + str(count)

print("Compressed string:", result)












