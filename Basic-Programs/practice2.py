# Find Maximum of two numbers in Python

def maximum(a,b):
     if a >= b:
        return a
     else:
        return b

a = eval(input("Enter first number:"))
b = eval(input("Enter second number:"))

print(maximum(a,b))
