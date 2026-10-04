from database.db import get_connection


def borrow_book(user_id, book_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT available
    FROM books
    WHERE id=?
    """, (book_id,))

    book = cursor.fetchone()

    if not book:

        conn.close()
        return False

    if book["available"] == 0:

        conn.close()
        return False

    # SAVE BORROW
    cursor.execute("""
    INSERT INTO borrowings(
        user_id,
        book_id,
        action_type
    )
    VALUES (?, ?, ?)
    """, (
        user_id,
        book_id,
        "borrow"
    ))

    cursor.execute("""
    UPDATE books
    SET available=0
    WHERE id=?
    """, (book_id,))

    conn.commit()
    conn.close()

    return True



def buy_book(user_id, book_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO borrowings(
        user_id,
        book_id,
        action_type
    )
    VALUES (?, ?, ?)
    """, (
        user_id,
        book_id,
        "buy"
    ))

    cursor.execute("""
    DELETE FROM books
    WHERE id=?
    """, (book_id,))

    conn.commit()
    conn.close()