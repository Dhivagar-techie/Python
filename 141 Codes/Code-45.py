# find it is a Happy NUmber

num=int(input("Enter the number:"))

temp=num

while temp!=1 and temp!=4:
    store=0
    while temp>0:
        squ=temp%10
        store+=squ**2
        temp=temp//10

    temp=store
    
if temp == 1:
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")