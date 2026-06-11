# Create a function that takes a single string as argument and returns an ordered listcontaining the indices of all capital letters in the string.

def index(string):
    store=[]
    for i in range(len(string)):
        if string[i].isupper():
            store.append(i)

    return store

obj=index("AbCdEf")
print(obj)
            