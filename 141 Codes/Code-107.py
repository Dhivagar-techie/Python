# Create a function that takes a string and returns a string in which each character isrepeated once.

def Repeated_funct(num):
    store=[]
    for i in num:
       A= i*2
       store.append(A)
    return "".join(store)
obj=Repeated_funct("hello")
print(obj)
