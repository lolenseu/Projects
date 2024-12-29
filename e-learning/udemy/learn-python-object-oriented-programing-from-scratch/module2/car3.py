class myCar:
    wheels = 4
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

car1 = myCar("Toyota", "Camry")
car2 = myCar("Honda", "Accord")

car1.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(myCar.wheels)