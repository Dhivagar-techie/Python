# Create a function that takes a list of non-negative integers and strings and return anew list without the strings.

def Filter(num):

    store=[]

    for i in num:
        if i.isdigit():
            store.append(i)
    
    return store 

print(Filter("123abc"))