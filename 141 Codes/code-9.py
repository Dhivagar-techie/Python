#Write a Python program to solve quadratic equation
import math

a=float(input("Enter the Value of A:"))
b=float(input("Enter the Value of B:"))
c=float(input("Enter the Value of C:"))

halfx=(b**2-(4*a*c))

if halfx>0:
    prob1=(-b + math.sqrt (halfx)) / 2*a
    prob2=(-b - math.sqrt (halfx)) / 2*a
    print("The value of Root1 And Root2:",prob1,prob2)

elif halfx == 0:
    prob3= (-b /(2*a))
    print("the value of Root:",prob3)

else :
    prob4= -b /2*a
    prob5= (math.sqrt (-halfx)) / 2*a
    print("The Value of root Realvalue and Imaginary value",prob4,prob5)