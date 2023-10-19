# Python Program for simple interest

def simpleInterest(p,t,r):
    si = (p*t*r)/100
    print("The simple interest is", si)

p = eval(input("Enter principal:"))
t = eval(input("Enter time period:"))
r = eval(input("Enter rate of interest:"))

simpleInterest(p,t,r)