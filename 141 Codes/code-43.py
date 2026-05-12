# Write a Python program to check if the given number is a Disarium Number.

num=int(input("Enter the number:"))

temp=num

string=str(temp)

store=0

for i in range(len(string)):

    store = store +  int(string[i])**(i+1)

if num==store:
    print(num," is a Disarium Number")

else:
    print(num," is not a Disarium Number")


