# Write a Python program to print all happy numbers between 1 and 100.


Start=int(input("Enter the first number:"))

End=int(input("Enter the Second number:"))

for i in range(Start,End+1):
    temp=i
    while temp!=1 and temp!=4:
        store=0
        while temp>0:
            squ=temp%10
            store+=squ**2
            temp=temp//10

        temp=store
        
    if temp == 1:
        print(i, "is a Happy Number")
    else:
        print(i, "is not a Happy Number")