def validate_register(data):

    if "username" not in data:
        return False, "Username is required"

    if "password" not in data:
        return False, "Password is required"

    if len(data["password"]) < 4:
        return False, "Password must contain at least 4 characters"

    return True, None



def validate_book(data):

    if "title" not in data:
        return False, "Title is required"

    if "author" not in data:
        return False, "Author is required"

    return True, None