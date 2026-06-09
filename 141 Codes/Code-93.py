# Create a function that takes an angle in radians and returns the corresponding anglein degrees rounded to one decimal place.

def radius_to_degree(rad):
    degree=rad*(180/3.14)
    return f"This is the Radius of {round(degree,2)}"

rad=int(input("enter the radius:"))

print(radius_to_degree(rad))

