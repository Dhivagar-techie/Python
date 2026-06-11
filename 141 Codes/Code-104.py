# assign variables from lists in a much more succinct way.Create variables first, middle and last from the given list using destructuringassignment 

list=[1,2,3,4,5,6,7,8,9,10]

first=list[0]
middle=list[1:-1]
last=list[-1:]

A=first,middle,last

for i in A:
    print (i)