# Write a Python program to sort Python Dictionaries by Key or Value

dict1 = {
    "apple": 50,
    "banana": 20,
    "orange": 40,
    "grapes": 10
}

sort=dict(sorted(dict1.items()))

key = dict(sorted(dict1.items(), key=lambda x: x[1]))

print(sort)
print(key)