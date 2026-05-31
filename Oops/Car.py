class Cares:
    def __init__(self,model,year,colour,sale):
        self.model=model
        self.year=year
        self.colour=colour
        self.sale=sale

    def drive(self):
        print(f"you drive the {self.colour} {self.model}")
    
    def stop(self):
        print(f"you stop the {self.colour}  {self.model}")

    def details(self):
        print(f"i have the {self.colour} {self.model} of { self.year} for {self.sale}")