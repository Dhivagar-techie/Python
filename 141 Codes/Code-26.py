# Write a Python Program to Make a Simple Calculator with 4 basic mathematicaloperations.
while True:
    print("1.Addition")
    print("2.Subration")
    print("3.Multiplication")
    print("4.Division")

    num=int(input("Enter Your Option :"))


    
    if num==1:
        sume=[]
        while True:
            
            n=float(input("Enter your number:"))
            sume.append(n)
            ans=input("Enter your Openion to add another number Yes/NO: :").lower().strip()
            if ans=="no":
                break
        print(sum(sume))

    elif num==2:
        store=[]
        while True:

            n=float(input("Enter your number:"))
            store.append(n)
            ans=input("Do you want to Add numbers for Subration Yes/NO :").lower().strip()
            if ans=="no":
                break
        temp1=store[0]
        for j in store[1:]:
            temp1=temp1-j

        print(temp1)

    elif num==3:
        store=[]
        while True:

            n=float(input("Enter your number:"))
            store.append(n)
            ans=input("Do you want to Add numbers Multiplication Yes/NO :").lower().strip()
            if ans=="no":
                break
        temp1=store[0]
        for j in store[1:]:
            temp1=temp1*j

        print(temp1)

    elif num==4:
        num1=int(input("Enter the First Number:"))
        num2=int(input("Enter the Second Number:"))

        if num1>num2:
            div=num1/num2
            print("Divided number will be:",div)
        elif num2==0:
            print("Number Cant be divided by zero, it leads to infinite")
        else:
            print("Error")
    else:
        print("Invalid Option")

    A=input("Do you want to run the program Again:").lower().split()
    if A=="No":
        break










