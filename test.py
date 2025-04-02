print("Hello World")
x = 5
y = "asd"
print(x,y)

list = [1,2,3,4,5]
list.append(6)
print(list)

list.pop()
print(list)

list.clear()
print(list)

dict = {"name" : "John", "age" : 30 , "city" : "New York"}
print(dict)

dict["country"] = "USA"
print(dict)

dict.pop("name")
print(dict)

for i in range(5):
    print(i)

i = 0
while i <= 5:
    print(i)
    i += 1

x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

def add(a, b):
    result = a + b
    return "The result is :" + str(result)
def subtract(a, b):
    result = a - b
    return "The result is :" + str(result)
def multiply(a, b):
    result = a * b
    return "The result is :" + str(result)
def divide(a, b):
    result = a / b
    return "The result is :" + str(result)

print(add(5,10))

def print_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


operation = "0"

while operation != "5":

    print_menu()
    operation = input("Enter the number of the operation you would like to calculate: ")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if operation == "1":
        print("Add")
        print(add(number1,number2))
    elif operation == "2":
        print("Subtract")
        print(subtract(number1,number2))
    elif operation == "3":
        print("Multiply")
        print(multiply(number1,number2))
    elif operation == "4":
        print("Divide")
        if number2 == "0" or number1 == "0":
            print("Cannot divide by 0")
        else:
            print(divide(number1,number2))
    elif operation == "5":
        print("Exit")
    else:
        print("Invalid character, try again.")
        

