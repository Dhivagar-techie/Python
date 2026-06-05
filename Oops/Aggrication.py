# Aggrication examples

class Libary:
    def __init__(self,name):
        self.name=name
        self.bookie=[]

    def Add_books(self,boo):
        self.bookie.append(boo)

    def List_books(self):
        return [f"{i.Auther} by {i.title}"for i in self.bookie]

    

class Books:
    def __init__(self,Auther,title):
        self.Auther=Auther
        self.title=title



Lib=Libary("pondy times")

book1=Books("ben10","MAn of Action")
book2=Books("POkiemon","Animal of Acid")
book3=Books("BAy blade","MAn of Anime")

Lib.Add_books(book1)
Lib.Add_books(book2)
Lib.Add_books(book3)

for j in Lib.List_books():
    print(j)
