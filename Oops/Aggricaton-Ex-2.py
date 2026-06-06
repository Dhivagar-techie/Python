class Library:

    def __init__(self, name):
        self.name = name


class Books:

    def __init__(self, library):
        self.library = library

    def display(self):
        print("Library Name:", self.library.name)


lib = Library("Pondy Times")

b1 = Books(lib)

b1.display()