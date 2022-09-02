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
    p1 = Book("Of Mice and Men", "John Stein")
    p2 = Book("To Kill A Mocking Bird", "Harper Lee")

    p1.display()
    p2.display()