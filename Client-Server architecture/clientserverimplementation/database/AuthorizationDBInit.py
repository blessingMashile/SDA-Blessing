import sqlite3

def initialize_authorization_requests_table():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('authorization_requests.db')
    cursor = conn.cursor()

    # Create the authorization_requests table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS authorization_requests (
                        bank_id TEXT,
                        terminal_id TEXT,
                        operation_code TEXT,
                        source_account TEXT,
                        destination_account TEXT,
                        transaction_sequence_number TEXT,
                        track_1_data TEXT,
                        track_2_data TEXT,
                        track_3_data TEXT,
                        pin_buffer TEXT,
                        transaction_amount TEXT,
                        surcharge_amount TEXT,
                        surcharge_enable_flag TEXT,
                        icc_data TEXT
                      )''')

    # Example data to insert into the authorization_requests table
    example_data = [
        ('123456', 'ABC12345', 'CW', 'CA', 'SA', '0001', '...', '...', '...', '1234567890123456', '10000', '100', '1', '...'),
        # Add more rows as needed
    ]

    # Insert example data into the authorization_requests table
    cursor.executemany('''INSERT INTO authorization_requests 
                          (bank_id, terminal_id, operation_code, source_account, destination_account, 
                          transaction_sequence_number, track_1_data, track_2_data, track_3_data, pin_buffer, 
                          transaction_amount, surcharge_amount, surcharge_enable_flag, icc_data) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', example_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Authorization requests table initialized with example data.")

# Call the function to initialize the authorization_requests table
initialize_authorization_requests_table()
