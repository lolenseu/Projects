class myCircle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 *self.radius ** 2
    

my_circle = myCircle(5)
print(f"Area: ", my_circle.area())