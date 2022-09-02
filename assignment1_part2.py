class Book:
    def __init__(self, author, title):
        """
        Constructor of a 'Book' class
        :param author: name of author
        :param title: title of book
        """
        self.author = author
        self.title = title

    def display(self):
        """prints string representing the book"""
        print(f"Book title: {self.author} Written by {self.title}")

if __name__ == "__main__":
    p1 = Book("Harry Potter and the Goblet of Fire", "J. K. Rowling")
    p2 = Book("Ivanhoe: A Romance", "Walter Scott")

    p1.display()
    p2.display()