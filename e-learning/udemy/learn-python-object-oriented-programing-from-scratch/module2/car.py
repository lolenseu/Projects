class myCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def description(self):
        return f"This car is a {self.brand} {self.model}"


my_car = myCar("Toyota", "Corolla")
print(my_car.description())