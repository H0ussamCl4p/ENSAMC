# This is a simple script to perform basic operations: addition, subtraction, multiplication, division, and modulo.

print("hello world")
print("This a script to do basic operations")
print("Addition, Soustraction, Multiplication, Division, Modulo")

def add(a, b):
    return a + b

def sous(a,b):
    return a - b

def mult(a,b):
    return a * b        

def div(a,b):       
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

def mod(a,b):
    return a % b


x = int(input("Please enter a: "))
y = int(input("Please enter b: "))

print("Addition: ", add(x, y))
print("Soustraction: ", sous(x, y))     
print("Multiplication: ", mult(x, y))
print("Division: ", div(x, y))
print("Modulo: ", mod(x, y))

