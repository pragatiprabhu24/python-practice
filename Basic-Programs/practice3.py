# Find the Factorial of a Number Using Recursive approach

def factorial(num):
    if(num==0 or num==1):
        return 1
    else:
        return num * factorial(num - 1)

num = eval(input("Enter number:"))
print("The factorial of", num, "is", factorial(num))