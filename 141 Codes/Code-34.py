# Write a Python Program for array rotation
def right(arr,d):
    sav=arr[d:]+arr[:d]
    return sav

def left(arr,d):
    sav=arr[-d:]+arr[:-d]
    return sav
 
arr=[12,2,34,1,45,78,56]
d=int(input("enter the number of rotations:"))
print("original Array",arr)

print("the array",d,"rotations after",right(arr,d))
print("the array",d,"rotations after",left(arr,d))
