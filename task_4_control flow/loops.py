# 1.Print numbers from 1 to 10 using a for loop.
print("1.Print numbers from 1 to 10 using a for loop.")
for i in range(1,11):
    print(i)

# 2.Print numbers from 10 to 1.
print("2.Print numbers from 10 to 1.")
for i in range(10,0,-1):
    print(i)

#3.Print all even numbers from 1 to 100.
print("3.Print all even numbers from 1 to 100.")

for i in range(1,100):
    if i%2==0:
        print(i)

#4.Print all odd numbers from 1 to 100.
print("4.Print all odd numbers from 1 to 100.")
for i in range(1,100):
    if i%2!=0:
        print(i)
#5.Print the multiplication table of a given number.
print("5.Print the multiplication table of a given number.")
for i in range(1,11):
    for j in range(1,11):
        print (i*j,end=" ")
    print()

#6.Count how many digits are present in a number.
print("6.Count how many digits are present in a number.")
number=int(input("Enter the number:"))
a=str(number)
print(len(a))

#7.Reverse a number.
print("7.Reverse a number.")
num=1234567
print("Given number:",num)
b=str(num)
print("reversed number:",(b[::-1]))

#8.Check whether a number is a palindrome.
print("Check whether a number is a palindrome")
if b[:]==b[::-1]:
    print("It is palindrome")
else:
    print("It is't palindrome")

#9.Check whether a number is prime.
print("9.Check whether a number is prime")
number1=54

if number1< 1:
    print("This is not a prime number")
else:
    is_prime=True
     
    for i in range(2,number1):
        if number1%i==0:
            is_prime=False
            break
       
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")

#10.Find the sum of n number.
print("10.Find the sum of n number")
n=10
sum=0
for i in range(1,n+1):
   
    sum+=i
    
print (sum)

#11.Find the sum of digits of a number.
print("11.Find the sum of digits of a number")
num1=11111
num2=str(num1)
sum1=0
for i in num2:
    sum1=sum1+int(i)
print(sum1)














