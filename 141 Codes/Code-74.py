# Write a program to calculate Q value

import math

C = 50
H = 30

D = input("Enter comma-separated values: ")

Sto=D.split(",")

store=[]

for i in Sto:
   d=int(i)
   j=math.sqrt((2*C*d)/H)
   store.append(str(int(j)))

print(",".join(store))



