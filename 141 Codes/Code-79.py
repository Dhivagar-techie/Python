# Write a program that accepts a sentence and calculate the number of letters anddigits. Suppose the following input is supplied to the program:

sentance=input("enter your sentances:")

number=0

letter=0

for i in sentance:
    if i.isalpha():
        number+=1
    elif i.isdigit():
        letter+=1

print("the total numbers are:",number)
print("the total letter are:",letter)
