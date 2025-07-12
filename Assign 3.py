# Task 1
# asking user to input a number
a = int(input("Enter a number: "))


# defining a function to obtain factorials
def factorial(a):
    if a < 2:
        return 1
    else:
        return a * (factorial(a - 1))


# calling the function and printing the result
result = factorial(a)
print(f"The factorial of {a} is : {result}")


# Task 2
# asking user to enter a number
a = int(input("Enter a number: "))


#importing math module
import math
# doing some calculations
print(f"Squareroot  of {a} : {math.sqrt(a)}")
print(f"logarith  of {a} : {math.log(a)}")
print(f"sine in radians  of {a} : {math.sin(a)}")