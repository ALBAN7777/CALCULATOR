def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
a=int(input("Enter a="))
b=int(input("Enter b="))
option=input("Enter option=")
if option == 'add':
    c = add(a, b)
    print(c)
elif option == 'subtract':
    c = subtract(a, b)
    print(c)
elif option == 'multiply':
    c = multiply(a, b)
    print(c)
elif option == 'divide':
    c = divide(a, b)
    print(c)
else:
    print("ERROR: Invalid option")
