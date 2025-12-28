class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"
    
class Ebook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Size: {self.file_size}MB"
    
class PrintedBook(Book):
    def __init__(self, title, author, price, weight):
        super().__init__(title, author, price)
        self.weight = weight
    
    def shipping_cost(self):
        return self.weight * 0.02

ebook1 = Ebook("Python Basics", "John Doe", 599, 5)
print(f"Ebook Info: {ebook1.get_info()}")

printed1 = PrintedBook("OOP Design","Alice Ray", 999, 500)
print(f"Printed Book Info: {printed1.get_info()}\nShipping Cost: {printed1.shipping_cost()}")
