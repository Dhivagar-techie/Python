# Write a Python program to print all disarium numbers between 1 to 100.

start=int(input("Enter the  first number:"))
end=int(input("Enter the second number:"))

for num in range(start,end+1):

    string=str(num)

    store=0

    for i in range(len(string)):

        store = store +  int(string[i])**(i+1)

    if num==store:
        print(num," is a Disarium Number")

    else:
        print(num," is not a Disarium Number")


