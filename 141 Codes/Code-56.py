#Write a Python program to Remove empty List from List.

lists = [[], [1, 2], [], [3, 4], [], [5]]

store=[]

for i in lists:
    if i:
       store.append(i)

print(store)