# Create a function that reverses a boolean value and returns the string "booleanexpected" if another variable type is given.

def Reverse(value):
    if value==True:
        return False
    elif value==False:
        return True

obj=Reverse(True)

print(obj)
      
# Alternative Method

def Reverse(value):
    if value=="True":
        return False
    elif value=="False":
        return True

obj=Reverse(True)

print(obj)
