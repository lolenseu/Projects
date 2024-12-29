class myDog:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        
    def bark(self):
        return f"{self.name} says woof"
    

my_dog = myDog("Buddy", "Golden Retriever")
print(my_dog.bark())
            