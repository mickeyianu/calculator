number1 = float(input("Number 1: "))
print(" ")
print("(1) Add \\n (2) Subtract \\n (3) Multiply \\n (4) Divide")
operation = input("Operation: ")
number2 = float(input("Number 2: "))

def add(number1, number2):
    return number1 + number2

def minus(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1 - number2

if operation == "1":
    print(add(number1, number2))

if operation == "2":
    print(minus(number1, number2))

if operation == "3":
    print(multiply(number1, number2))

if operation == "4":
    print(divide(number1, number2))
