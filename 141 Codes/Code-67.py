# Write a Python program to Extract Unique dictionary values.

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

store=data.values()

hii=set(store)

print(hii)