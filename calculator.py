def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
    
while True:
    a = input("Enter a (or 'q' to quit): ")
    if a == 'q':
        break

    b = float(input("Enter b: "))
    option = input("Enter option : ")

    if option == 'add':
        c = add(float(a), b)
        print(c)
    elif option == 'subtract':
        c = subtract(float(a), b)
        print(c)
    elif option == 'multiply':
        c = multiply(float(a), b)
        print(c)
    elif option == 'divide':
        c = divide(float(a), b)
        print(c)
    else:
        print("ERROR: Invalid option")



