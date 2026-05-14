# find the N largest numbers

Array = [12, 3, 57, 78, 3, 223, 56, 4]

num=int(input("Enter the numbers:"))

duplicate=list(set(Array))

duplicate.sort(reverse=True)

A=duplicate[:num]

print(A)