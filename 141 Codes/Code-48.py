# A Pronic number

num=int(input("enter the number:"))

flag=0

for i in range(1,num+1):
    if ((i*(i+1))==num):
        flag=1
        break

if flag==1:
    print(num,"this is a pronic number")
else:
    print(num,"this is not a pronic number")