import requests

BASE_URL = "http://127.0.0.1:5000"

token = None
role = None


def register():

    username = input("Username: ")
    password = input("Password: ")
    role_input = input(
        "Role (admin/user): "
    )

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={
            "username": username,
            "password": password,
            "role": role_input
        }
    )

    print(response.json())



def login():

    global token
    global role

    username = input("Username: ")
    password = input("Password: ")

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "username": username,
            "password": password
        }
    )

    if response.status_code == 200:

        data = response.json()

        token = data["token"]
        role = data["role"]

        print("Login successful")

        dashboard()

    else:

        print("Invalid credentials")



def get_headers():

    return {
        "Authorization":
        f"Bearer {token}"
    }



def show_books():

    response = requests.get(
        f"{BASE_URL}/books/",
        headers=get_headers()
    )

    books = response.json()

    print("\n===== BOOKS =====")

    for book in books:

        print(f"""
ID: {book['id']}
Title: {book['title']}
Author: {book['author']}
Description: {book['description']}
Available: {book['available']}
""")


    return books



def borrow_book():

    book_id = input(
        "Book ID to borrow: "
    )

    response = requests.post(
        f"{BASE_URL}/borrow/borrow/{book_id}",
        headers=get_headers()
    )

    print(response.json())



def buy_book():

    book_id = input(
        "Book ID to buy: "
    )

    response = requests.post(
        f"{BASE_URL}/borrow/buy/{book_id}",
        headers=get_headers()
    )

    print(response.json())



def add_book():

    title = input("Title: ")
    author = input("Author: ")
    description = input("Description: ")

    response = requests.post(
        f"{BASE_URL}/books/",
        headers=get_headers(),
        json={
            "title": title,
            "author": author,
            "description": description
        }
    )

    print(response.json())



def delete_book():

    title = input(
        "Book title to delete: "
    )

    response = requests.delete(
        f"{BASE_URL}/books/delete-by-name/{title}",
        headers=get_headers()
    )

    print(response.json())



def update_book():

    book_id = input("Book ID: ")

    title = input("New Title: ")
    author = input("New Author: ")
    description = input("New Description: ")

    response = requests.put(
        f"{BASE_URL}/books/{book_id}",
        headers=get_headers(),
        json={
            "title": title,
            "author": author,
            "description": description
        }
    )

    print(response.json())



def dashboard():

    global role

    while True:

        # USER
        if role == "user":

            print("""
===== USER DASHBOARD =====

1. Show Books
2. Borrow Book
3. Buy Book
4. Logout
""")

            choice = input("Choice: ")

            if choice == "1":
                show_books()

            elif choice == "2":
                show_books()
                borrow_book()

            elif choice == "3":
                show_books()
                buy_book()

            elif choice == "4":
                break


        # ADMIN
        if role == "admin":

            print("""
===== ADMIN DASHBOARD =====

1. Show Books
2. Add Book
3. Update Book
4. Delete Book
5. Logout
""")

            choice = input("Choice: ")

            if choice == "1":
                show_books()

            elif choice == "2":
                add_book()

            elif choice == "3":
                show_books()
                update_book()

            elif choice == "4":
                show_books()
                delete_book()

            elif choice == "5":
                break



while True:

    print("""
===== LIBRARY SYSTEM =====

1. Register
2. Login
3. Exit
""")

    choice = input("Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break