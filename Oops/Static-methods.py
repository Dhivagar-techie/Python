# This is A Example of Static methods

class Company:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def get_details(self):
        return f"{self.name} is a employee with {self.position} position"

    @staticmethod
    def check_position(position):
        v_position=["manager","server","cashier","Janitor"]
        if position.lower() in v_position:
            return position.lower()
        else:
            return "invalid Position"


comp1=Company("red ranger","leader")
comp2=Company("green ranger","side chick")
comp3=Company("yellow ranger","comedian")

print(comp1.get_details())
print(comp2.get_details())
print(comp3.get_details())

print(Company.check_position("mAnager"))