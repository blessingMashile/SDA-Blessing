import sqlite3

def initialize_authorization_responses_table():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('authorization_responses.db')
    cursor = conn.cursor()

    # Create the authorization_responses table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS authorization_responses (
                        bank_id TEXT,
                        terminal_id TEXT,
                        local_transaction_date TEXT,
                        local_transaction_time TEXT,
                        retrieval_reference_number TEXT,
                        requested_dollar_amount TEXT,
                        dispensed_dollar_amount TEXT,
                        surcharge_amount TEXT,
                        surcharge_enable_flag TEXT,
                        icc_data TEXT
                      )''')

    # Example values to insert into the authorization_responses table
    example_values = [
        ('123456', 'ABC12345', '01012022', '123456', '123456789012',
         '10000', '10000', '0', '0', '...')
    ]

    # Insert example values into the authorization_responses table
    cursor.executemany('''INSERT INTO authorization_responses 
                          (bank_id, terminal_id, local_transaction_date, local_transaction_time, 
                           retrieval_reference_number, requested_dollar_amount, dispensed_dollar_amount,
                           surcharge_amount, surcharge_enable_flag, icc_data) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', example_values)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Authorization Responses table initialized with example values.")

# Call the function to initialize the authorization_responses table
initialize_authorization_responses_table()
