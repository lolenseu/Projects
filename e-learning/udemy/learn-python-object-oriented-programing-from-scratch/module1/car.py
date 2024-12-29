class myCar:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        
    def start(self):
        return f"{self.model} is starting."
    
    def stop(self):
        return f"{self.model} is stopping."
    

myCar = myCar("Red", "Toyoto Camry", 2022)
myAnotherCar = myCar("Black", "Tesla model x", 2025)

print(myCar.color)
print(myCar.model)
print(myCar.start())

print()

print(myAnotherCar.color)
print(myAnotherCar.model)
print(myAnotherCar.start())
