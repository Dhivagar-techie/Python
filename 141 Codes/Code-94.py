# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is aCurzon number.
#Given a non-negative integer num, implement a function that returns True if num is aCurzon number, or False otherwise.

def cuzon_number(num):
    Sto=((2**num)+1)%(2*num+1)
    if Sto==0:
        print (Sto)
        return True
        
    else:
        print (Sto)
        return False

num=int(input("enter your number:"))

print(cuzon_number(num))

