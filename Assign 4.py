
#Task 1:
#open file to read its content
try:
    with open('sample.txt','r+') as fl:
        print(fl.read())
except FileNotFoundError as e:
    print("The file sample.txt not found.")
finally:
    print("\n Task completed")



#Task 2:

a=str(input("Enter text to write in file : "))
try: 
    with open ('output.txt', 'w') as file1:
        file1.write(a + "\n")
        print("Text written to file successfully.")
except fileNotFoundError:
    print("The file was not found.")
finally:
    print("Enter additiional text to append: ")
    b=str(input())  

with open ('output.txt', 'a') as file1:
    file1.write(b + "\n")
    print("Additional text appended to file successfully.")

with open ('output.txt', 'r') as file1:
    print(file1.read())