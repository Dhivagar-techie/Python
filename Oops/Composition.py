# this is the Example of composition 

class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power
    
    def start(self):
        print(f"Engine has Started with Power of {self.horse_power}CC...")

    def stop(self):
        print(f"Engine has stopped")

class Car:
    def __init__(self,name,Model,horse_power):
        self.name=name
        self.Model=Model
        self.engine=Engine(horse_power)

    def start(self):
        print(f"engine started for {self.name} with power of {self.Model}")
        self.engine.start()

    def stop(self):
        print(f"Engine has been Stopped for {self.name}")
        self.engine.stop()
    

Cars=Car("BMW","1000RR",800)
eng=Engine(1000)

Cars.start()
Cars.stop()
eng.start()
eng.stop()
    


