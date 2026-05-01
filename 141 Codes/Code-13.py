#Write a Python Program to Check Leap Year.

Year = int(input("Enter the Year: "))

if (Year%4==0 and Year%100!=0) or (Year%400==0):
    print(Year," is a Leap Year")
else:
   print(Year,"is a  Not a Leap Year")