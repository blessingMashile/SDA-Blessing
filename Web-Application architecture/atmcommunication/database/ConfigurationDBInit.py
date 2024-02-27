import sqlite3

def initialize_configuration_table():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('configuration.db')
    cursor = conn.cursor()

    # Create the configuration table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS configuration (
                        id INTEGER PRIMARY KEY,
                        setting TEXT
                      )''')

    # Example settings to insert into the configuration table
    example_settings = [
        ('Example setting 1',),
        ('Example setting 2',),
        ('Example setting 3',)
    ]

    # Insert example settings into the configuration table
    cursor.executemany('INSERT INTO configuration (setting) VALUES (?)', example_settings)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Configuration table initialized with example settings.")

# Call the function to initialize the configuration table
initialize_configuration_table()
