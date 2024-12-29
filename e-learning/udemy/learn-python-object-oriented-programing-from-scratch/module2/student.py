class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def introduce(self):
        return f"My name is {self.name}, and I am grade {self.grade}."
    

student1 = Student("Alice", "10th")
student2 = Student("Bob", "12th")

print(student1.introduce())
print(student2.introduce())