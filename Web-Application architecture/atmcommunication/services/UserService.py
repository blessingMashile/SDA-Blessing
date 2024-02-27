import sqlite3
from werkzeug.security import check_password_hash


# Function to verify user credentials
def verify_user(username, password):
    # You can replace this with your database logic to check if the username and password are valid
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password_hash FROM users WHERE username=?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        # Check if the password hash matches
        password_hash = result[0]
        return check_password_hash(password_hash, password)
    else:
        return False
