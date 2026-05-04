#  Find the HCF of the Two Numbers
n1=int(input("Enter the first Number:"))
n2=int(input("Enter the Second Number:"))

small_num=min(n1,n2)

for i in range(1,small_num+1):
    if(n1%i==0) and (n2%i==0):
        hcf=i
print(hcf,"is the HCF")
