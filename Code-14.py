# Check Wheather the Numberes are prime are not

num=int(input("Enter the number to check :"))
prime=True
if num>1:
    for i in range (2,num):
      if num%i==0:
        prime=False
        break
    if prime:
        print(num," is a prime Number")
    else:
        print(num," is a  Not a prime Number") 
else:
    print(num,"is not a Prime Number")


