# Python Program for Compound Interest

def CompoundInterest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    print("The Compound Interest is", ci)

principal = eval(input("Enter principal:"))
rate = eval(input("Enter rate:"))
time = eval(input("Enter time:"))

CompoundInterest(principal, rate, time)

