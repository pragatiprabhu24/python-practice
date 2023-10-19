# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

num1 = eval(input("Enter first number"))
num2 = eval(input("Enter second number"))

product = num1 * num2
sum = num1 + num2

if(product <= 1000):
    print("The result is", product)
else:
    print("The result is", sum)
    