import sqlite3

def initialize_authorization_requests_table():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('authorization_requests.db')
    cursor = conn.cursor()

    # Create the authorization_requests table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS authorization_requests (
                        protocol_dependent_header TEXT,
                        record_format TEXT,
                        application_type TEXT,
                        bank_id TEXT,
                        terminal_id TEXT,
                        request_type TEXT,
                        unknown_value_field TEXT,
                        protocol_dependent_trailer TEXT
                      )''')

    # Example values to insert into the authorization_requests table
    example_values = [
        ('protocol_dependent_header_value', 'record_format_value', 'application_type_value',
         'bank_id_value', 'terminal_id_value', 'request_type_value',
         'unknown_value_field_value', 'protocol_dependent_trailer_value')
    ]

    # Insert example values into the authorization_requests table
    cursor.executemany('''INSERT INTO authorization_requests 
                          (protocol_dependent_header, record_format, application_type, 
                           bank_id, terminal_id, request_type, 
                           unknown_value_field, protocol_dependent_trailer) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', example_values)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Authorization Requests table initialized with example values.")

# Call the function to initialize the authorization_requests table
initialize_authorization_requests_table()
