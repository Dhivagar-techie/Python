# Create a function that takes the height and radius of a cone as arguments and returnsthe volume of the cone rounded to the nearest hundredth. See the resources tab forthe formula.

def radius_of_cone(height,radius):
    if height ==0 or radius == 0:
        return f"height and cone cant be Zero"
    volume=(1/3)*(3.14)*(radius**2)*height
    return round(volume,2)

obj=radius_of_cone(23,5)

print(obj)

