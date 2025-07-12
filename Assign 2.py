# Task 1: asking a number from user to check whether it is odd or even
a=int(input("Enter a number: "))

if a%2==0:
    print(str(a) +" is even number")
else:
    print(str(a) +" is odd number")

# Task 2: sum of integers from 1 to 50

a=int(input("Enter first number:  ")) #Enter 1
b=int(input("Enter last number:  ")) #Enter 51
c=int(input("Enter step:  ")) #Enter 1

d = list(range(a, b, c))
#print(d)
print(f"The sum of numbers from {a} to {b-1} is {sum(d)}")