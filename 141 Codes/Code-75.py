# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensionalarray. The element value in the i-th row and j-th column of the array should be i*j.

x,y=map(int,input("enter the values:").split(","))

array=[]

for i in range(x):

    store=[]

    for j in range(y):

        s=i*j

        store.append(s)
    array.append(store)
    

print(array)
