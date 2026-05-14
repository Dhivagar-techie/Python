# Write a Python program to Count occurrences of an element in a list.

numbers = [1, 2, 3, 2, 4, 2, 5]

element=2

num=numbers.count(element)

print(num)

# method 2

numbers = [1, 2, 3, 2, 4, 2, 5]

element = 2

count=0

for j in numbers:
    if j == element:
        count+=1

print(count)





