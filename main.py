
try:
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the 2nd number"))
except ValueError:
    print("thats not a number!!")

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2
operator = int(input("enter 1 for add, 2 for minus, 3 for times, and 4 for division"))

try:
    if operator == 4:

        print(divide(num1,num2))
    elif operator == 1:
        print(add(num1,num2))
    elif operator == 2:
        print(subtract(num1,num2))
    elif operator == 3:
        print(multiply(num1,num2))
except ZeroDivisionError:
    print("oi you CANT divide with 0 mate")
except ValueError:
    print("that aint no number")
