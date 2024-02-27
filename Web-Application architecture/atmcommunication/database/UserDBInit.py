import sqlite3
from werkzeug.security import generate_password_hash

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password_hash TEXT NOT NULL
                  )''')

# Insert example data with password hashes
example_data = [
    ('john', generate_password_hash('password123')),
    ('emma', generate_password_hash('password456'))
]

cursor.executemany('INSERT INTO users (username, password_hash) VALUES (?, ?)', example_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Example data with password hashes added to the users.db database.")
