class myCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = myCar("Toyota", "Camry")
print(my_car.brand)

my_car.brand = "Corolla"
print(my_car.brand)