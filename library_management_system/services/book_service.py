from database.db import get_connection


def add_book(title, author, description):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO books(
        title,
        author,
        description
    )
    VALUES (?, ?, ?)
    """, (
        title,
        author,
        description
    ))

    conn.commit()
    conn.close()



def get_books():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM books
    """)

    books = cursor.fetchall()

    conn.close()

    return books



def update_book(
    book_id,
    title,
    author,
    description
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE books
    SET title=?,
        author=?,
        description=?
    WHERE id=?
    """, (
        title,
        author,
        description,
        book_id
    ))

    conn.commit()
    conn.close()



def delete_book(book_title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM books
    WHERE title=?
    """, (book_title,))

    conn.commit()
    conn.close()