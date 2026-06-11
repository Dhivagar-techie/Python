# Given a list of numbers, create a function which returns the list but with eachelement's index in the list added to itself. This means you add 0 to the number atindex 0, add 1 to the number at index 1, etc...

def Add_index(list):
    count=[]
    for i in range(len(list)):
       A= i+list[i]
       count.append(A)
    return count

obj=Add_index([1,2,3,4,5,6,7,8,9])
print(obj)