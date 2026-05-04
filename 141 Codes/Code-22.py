#Find the LCM of Two numbers
n1=int(input("Enter the first Number:"))
n2=int(input("Enter the Second Number:"))

if n1>n2:
    biggest = n1
else:
    biggest = n2

while True:
        if (biggest%n1==0) and (biggest%n2==0):
            final=biggest
            break
        biggest=biggest+1
      
print(final)