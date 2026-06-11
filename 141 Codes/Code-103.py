# The "Reverser" takes a string as input and returns that string in reverse order, withthe opposite case.

def reverse(values):

    convert=values[::-1]

    return convert


values=input("enter your string:")

print(reverse(values))