# Please write a program using generator to print the even numbers between 0 and n incomma separated form while n is input by console.

def Even_num(n):
    for i in range(n+1):
       if i%2==0:
        yield str(i)

n=int(input("enter the number:"))


print(",".join(Even_num(n)))
