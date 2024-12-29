class myBook:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author
        
    def details(self):
        return f"'{self.title}' by {self.author}"


my_book = myBook("1984", "George Orwell")
author_book = myBook("Untitled")

print(my_book.details())
print(author_book.details())