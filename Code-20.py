num1=int(input("Enter then first number"))
num2=int(input("Enter then Second number"))


if num1<0 or num2<0:
    print("Error , NUmber Can't be below zero")
else:
    for i in range (num1,num2+1):
        temp=0
        nofo=i
        leng=len(str(i))

        while nofo>0:
          sav=nofo%10 
          temp =  (sav**leng) + temp
          nofo=nofo//10

        if temp==i:
            print(i,"list of amstrong numbers ")
        
          


        

