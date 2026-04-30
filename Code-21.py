#Write a Python Program to Find the Sum of Natural Numbers.

end_num=int(input("enter the ending number: "))

temp=0
for i in range(1,end_num+1):
    temp=temp+i
print(temp)

"""
n = int(input("Enter number: "))
print(sum(range(1, n + 1)))

"""