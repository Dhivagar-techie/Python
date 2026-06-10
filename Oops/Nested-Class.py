# Nested class Examples

class company:
    class Emplyoee:
        def __init__(self,name,position):
            self.name=name
            self.position=position
        
        def get_details(self):
           return f"{self.name}is working on {self.position}"
    
    def __init__(self,company_name):
        self.company_name=company_name
        self.Employees=[]

    def Add_employee(self,name,position):
        new_employee=self.Emplyoee(name,position)
        self.Employees.append(new_employee)

    def List_employee(self):
        return [i.get_details() for i in self.Employees]


cope_name=company("gravity Falls")

cope_name.Add_employee("Copper","Manager")
cope_name.Add_employee("Alex","Developer")
cope_name.Add_employee("MAddy","Skeleton")


for j in cope_name.List_employee():
    print(j)
