class myDog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
dog1 = myDog("Buddy", 5)   
dog2 = myDog("Milo", 3)

print(dog1.name)
print(dog2.age)
print(dog1.species)