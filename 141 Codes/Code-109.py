# Create a function that returns the thickness (in meters) of a piece of paper afterfolding it n number of times. The paper starts off with a thickness of 0.5mm.

def thickness(times):

    constant=0.5

    sto=constant*(2**times)

    converted= sto/1000

    return round(converted,2)

obj=thickness(9)

print(obj)