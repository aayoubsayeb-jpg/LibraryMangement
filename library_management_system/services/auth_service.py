from database.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(username, password, role="user"):
    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = generate_password_hash(password)

    try:
        cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, (username, hashed_password, role))

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user["password"], password):
        return user

    return None