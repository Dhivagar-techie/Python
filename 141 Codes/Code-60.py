# Write a Python program to find smallest number in a list.

Array=[12,34,56,2,34,879,12]

store=Array[0]

for i in Array:
    if store>i:
        store=i

print(store)

