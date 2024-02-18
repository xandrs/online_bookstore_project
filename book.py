class Book:
    # __init__ method allows to initialize the state of objects when they are created, ensuring that
    # they are created with the necessary attributes and initial values.
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def add_single_book(self):
        # Add a single copy of the book to the inventory.
        self.quantity += 1

    def add_multiple_books(self, quantity):
        # Add multiple copies of the book to the inventory.
        # Args:
        #     quantity (int): The number of copies to add.
        self.quantity += quantity

    def __str__(self):
        return f"{self.title} by {self.author}"

# # Test code
if __name__ == "__main__":
    # Create a new book object
    my_book = Book("Python Programming", "John Smith", 29.99, 10)

    # Add a single copy of the book
    my_book.add_single_book()

    # Add multiple copies of the book
    my_book.add_multiple_books(5)

    # Print book details
    print(my_book)
    print(f"Quantity in inventory: {my_book.quantity}")

# Output
# Python Programming by John Smith
# Quantity in inventory: 16
