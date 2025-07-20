
#Task 1
#Creating  an example of dicitionary in Python
a= {"cb":90,"sk":86,"HS":4, "Dk":71,"john":27,"DD":100}
#print(a)

#Asking user to input a key (name) to search in the dictionary

b= input("Enter the student's name: ")

#printing marks of student name entered by user

#print("{}'s marks : {}".format(b, a.get(b, " Student Not found")

if b in a:
    print( "{}'s marks: {}".format(b,a[b]))
else:
    print("student not found")


#Task 2
#Creating  a list of numbers from 1 to 10
x= list(range(1, 11))
print( f"original list : {x}")
# first 5 elements from the list
a=x[0:5]
print(f"Extracted first five elements: {a}")
# reverse the list
a.reverse()
print("Reversed extracted elements : {}".format(a))
