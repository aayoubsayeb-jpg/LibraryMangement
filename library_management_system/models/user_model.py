class User:

    def __init__(self, id, username, role):

        self.id = id
        self.username = username
        self.role = role


    def to_dict(self):

        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }