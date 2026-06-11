# Create a function that takes a list of strings and integers, and filters out the list sothat it returns a list of integers only.

def filter(string):
    store=[]
    for i in string:
        if str(i).isdigit():
            store.append(i)
    return store

obj=filter([9971,28,39,"a1j","jb"])

print(obj)
