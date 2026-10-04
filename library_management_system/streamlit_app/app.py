import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Library System",
    layout="wide"
)

# SESSION
if "token" not in st.session_state:
    st.session_state.token = None

if "role" not in st.session_state:
    st.session_state.role = None


# LOGIN / REGISTER
if not st.session_state.token:

    st.title("📚 Library Management System")

    option = st.selectbox(
        "Choose Option",
        ["Login", "Register"]
    )

    # REGISTER
    if option == "Register":

        st.subheader("Create Account")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            ["user", "admin"]
        )

        if st.button("Register"):

            response = requests.post(
                f"{BASE_URL}/auth/register",
                json={
                    "username": username,
                    "password": password,
                    "role": role
                }
            )

            if response.status_code == 201:

                st.success(
                    "Registration successful"
                )

            else:

                st.error(
                    response.json()
                )

    # LOGIN
    if option == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            response = requests.post(
                f"{BASE_URL}/auth/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.token = data["token"]
                st.session_state.role = data["role"]

                st.rerun()

            else:

                st.error(
                    "Invalid credentials"
                )

# DASHBOARD
else:

    headers = {
        "Authorization":
        f"Bearer {st.session_state.token}"
    }

    st.sidebar.success(
        f"Connected as {st.session_state.role}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.token = None
        st.session_state.role = None

        st.rerun()

    response = requests.get(
        f"{BASE_URL}/books/",
        headers=headers
    )

    # IMPORTANT FIX
    if response.status_code == 200:

        books = response.json()

    else:

        st.error(response.text)
        books = []

    st.title("📚 Library Dashboard")

    # USER PAGE
    if st.session_state.role == "user":

        st.subheader("Available Books")

        for book in books:

            with st.container():

                st.markdown("---")

                st.subheader(book["title"])

                st.write(
                    f"✍️ Author: {book['author']}"
                )

                st.write(
                    f"📝 Description: {book['description']}"
                )

                status = (
                    "✅ Available"
                    if book["available"]
                    else "❌ Borrowed"
                )

                st.write(status)

                col1, col2 = st.columns(2)

                # BORROW
                with col1:

                    if book["available"]:

                        if st.button(
                            f"Borrow {book['id']}"
                        ):

                            requests.post(
                                f"{BASE_URL}/borrow/borrow/{book['id']}",
                                headers=headers
                            )

                            st.success(
                                "Book borrowed"
                            )

                            st.rerun()

                # BUY
                with col2:

                    if st.button(
                        f"Buy {book['id']}"
                    ):

                        requests.post(
                            f"{BASE_URL}/borrow/buy/{book['id']}",
                            headers=headers
                        )

                        st.success(
                            "Book purchased"
                        )

                        st.rerun()

    # ADMIN PAGE
    if st.session_state.role == "admin":

        st.subheader("⚙️ Admin Dashboard")

        st.markdown("## ➕ Add Book")

        title = st.text_input("Title")
        author = st.text_input("Author")
        description = st.text_area("Description")

        if st.button("Add Book"):

            requests.post(
                f"{BASE_URL}/books/",
                headers=headers,
                json={
                    "title": title,
                    "author": author,
                    "description": description
                }
            )

            st.success("Book Added")

            st.rerun()

        st.markdown("---")

        st.markdown("## 📚 Manage Books")

        for book in books:

            with st.expander(book["title"]):

                new_title = st.text_input(
                    f"Title {book['id']}",
                    value=book["title"]
                )

                new_author = st.text_input(
                    f"Author {book['id']}",
                    value=book["author"]
                )

                new_description = st.text_area(
                    f"Description {book['id']}",
                    value=book["description"]
                )

                col1, col2 = st.columns(2)

                # UPDATE
                with col1:

                    if st.button(
                        f"Update {book['id']}"
                    ):

                        requests.put(
                            f"{BASE_URL}/books/{book['id']}",
                            headers=headers,
                            json={
                                "title": new_title,
                                "author": new_author,
                                "description": new_description
                            }
                        )

                        st.success("Updated")

                        st.rerun()

                # DELETE
                with col2:

                    if st.button(
                        f"Delete {book['id']}"
                    ):

                        requests.delete(
                            f"{BASE_URL}/books/delete-by-name/{book['title']}",
                            headers=headers
                        )

                        st.success("Deleted")

                        st.rerun()