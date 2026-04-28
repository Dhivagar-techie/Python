# Write a Python Program to Print all Prime Numbers in an Interval of 1-10

num1=int(input("Enter the First NUmber :"))
num2=int(input("Enter the Second NUmber :"))

if num1>num2:
    print("Error 2nd number was bigger")
else:
   for i in range (num1,num2+1):
     if i>1:
        for j in range (2,i):
            if i%j==0:
                break
        else:
          print(i)

     


