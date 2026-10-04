class Book:

    def __init__(self, id, title, author, available=1):

        self.id = id
        self.title = title
        self.author = author
        self.available = available


    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }