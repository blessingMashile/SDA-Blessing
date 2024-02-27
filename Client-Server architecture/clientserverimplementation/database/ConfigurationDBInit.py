import sqlite3

def initialize_message_table():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()

    # Create the message table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY,
                        protocol_dependent_header TEXT,
                        record_format TEXT,
                        application_type TEXT,
                        bank_id TEXT,
                        terminal_id TEXT,
                        request_type TEXT,
                        unknown_value_field TEXT,
                        protocol_dependent_trailer TEXT
                      )''')

    # Example message values
    example_messages = [
        ("header1", "format1", "type1", "bank1", "terminal1", "request1", "unknown1", "trailer1"),
        ("header2", "format2", "type2", "bank2", "terminal2", "request2", "unknown2", "trailer2"),
        ("header3", "format3", "type3", "bank3", "terminal3", "request3", "unknown3", "trailer3")
    ]

    # Insert example messages into the messages table
    cursor.executemany('''INSERT INTO messages (protocol_dependent_header, record_format,
                        application_type, bank_id, terminal_id, request_type,
                        unknown_value_field, protocol_dependent_trailer)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', example_messages)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Message table initialized with example messages.")

# Call the function to initialize the message table
initialize_message_table()
