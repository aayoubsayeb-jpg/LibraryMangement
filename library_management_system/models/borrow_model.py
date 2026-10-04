class Borrow:

    def __init__(self, id, user_id, book_id, borrow_date):

        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date


    def to_dict(self):

        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date
        }