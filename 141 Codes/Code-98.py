# Create a function that returns True if a given inequality expression is correct andFalse otherwise.

def Evaluee(a,operation,b):
    if operation=="<":
        return a<b
    elif operation==">":
        return a>b
    elif operation=="<=":
        return a<=b
    elif operation==">":
        return a>=b
    elif operation=="==":
        return a==b

num1 = int(input("Enter the a: "))
oper = input("Enter the operation: ")
num2 = int(input("Enter the c: "))

A=Evaluee(num1,oper,num2)
print(A)

# Alternative Method

def check_inequality(expression):
    return eval(expression)


print(check_inequality("3 < 7 < 11"))
print(check_inequality("13 > 44 > 33 > 1"))


