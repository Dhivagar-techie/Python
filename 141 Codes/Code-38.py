#Multiplication of two Matrix

a=int(input("Enter the number of rows:"))
b=int(input("Enter the number of coloums:"))

totalA=[]

for i in range(a):
    Onlyrowa=[]
    for j in range(b):
        val=int(input(f"enter  the a[{i}][{j}]"))
        Onlyrowa.append(val)
    totalA.append(Onlyrowa)



totalB=[]

for i in range(a):
    Onlyrowb=[]
    for j in range(b):
        val=int(input(f"enter  the a[{i}][{j}]:"))
        Onlyrowb.append(val)
    totalB.append(Onlyrowb)




total=[]

for i in range(a):
    Onlyrowc=[]
    for j in range(b):
        val=totalA[i][j] * totalB[i][j]
        Onlyrowc.append(val)
    total.append(Onlyrowc)

print("the matrix of A",totalA)

print("the matrix of B",totalB)

print("the Multiplicaton of A+B",total)




