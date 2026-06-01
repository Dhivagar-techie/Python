class student:
   
    graduate=2025
    noofstud=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.noofstud+=1

stud1=student("Ben",20)
stud2=student("Quen",22)
stud3=student("gradpa",40)
stud4=student("Kevin",25)


print(f"In My Class {student.noofstud} Students has when I graduate At {student.graduate}")

