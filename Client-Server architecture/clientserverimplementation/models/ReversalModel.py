#Reversal server
import sqlite3


class ReversalRequestMessage:
    def __init__(self, bank_id, terminal_id, local_transaction_date, local_transaction_time,
                 retrieval_reference_number, requested_dollar_amount, dispensed_dollar_amount,
                 surcharge_amount, surcharge_enable_flag, icc_data):
        self.protocol_dependent_header = ""
        self.record_format = "H"
        self.application_type = "0"
        self.message_delimiter = "."
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.request_type = "86"
        self.local_transaction_date = local_transaction_date
        self.local_transaction_time = local_transaction_time
        self.retrieval_reference_number = retrieval_reference_number
        self.requested_dollar_amount = requested_dollar_amount
        self.dispensed_dollar_amount = dispensed_dollar_amount
        self.surcharge_amount = surcharge_amount
        self.surcharge_enable_flag = surcharge_enable_flag
        self.icc_data = icc_data
        self.protocol_dependent_trailer = ""

    def generate_message(self):
        message = (
            f"{self.protocol_dependent_header}{self.record_format}{self.application_type}"
            f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}:{self.request_type}:"
            f"{self.local_transaction_date}:{self.local_transaction_time}:{self.retrieval_reference_number}:"
            f"{self.requested_dollar_amount}:{self.dispensed_dollar_amount}:{self.surcharge_amount}:"
            f"{self.surcharge_enable_flag}:{self.icc_data}{self.protocol_dependent_trailer}"
        )
        return message


# Example usage
reversal_request = ReversalRequestMessage(
    bank_id="123456",
    terminal_id="ABC12345",
    local_transaction_date="01012022",
    local_transaction_time="123456",
    retrieval_reference_number="123456789012",
    requested_dollar_amount="10000",
    dispensed_dollar_amount="10000",
    surcharge_amount="0",
    surcharge_enable_flag="0",
    icc_data="...",
)

generated_message = reversal_request.generate_message()
print("Generated Reversal Request Message:")
print(generated_message)

class ReversalResponseMessage:
    def __init__(self, bank_id, terminal_id, configuration_request_initiator, icc_data):
        self.protocol_dependent_header = ""
        self.record_format = "H"
        self.application_type = "0"
        self.message_delimiter = "."
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.response_type = "86"
        self.configuration_request_initiator = configuration_request_initiator
        self.icc_data = icc_data
        self.protocol_dependent_trailer = ""

    def generate_message(self):
        # Connect to SQLite database
        conn = sqlite3.connect('authorization_requests.db')
        cursor = conn.cursor()

        # Insert authorization response into database
        cursor.execute('''INSERT INTO authorization_responses VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (reversal_request.bank_id, reversal_request.terminal_id,
                        reversal_request.local_transaction_date, reversal_request.local_transaction_time,
                        reversal_request.retrieval_reference_number,
                        reversal_request.surcharge_amount,  reversal_request.icc_data))

        conn.commit()

        # Close the database connection
        conn.close()
        message = (
            f"{self.protocol_dependent_header}{self.record_format}{self.application_type}"
            f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}:{self.response_type}:"
            f"{self.configuration_request_initiator}:{self.icc_data}{self.protocol_dependent_trailer}"
        )
        return message


# Example usage
reversal_response = ReversalResponseMessage(
    bank_id="123456",
    terminal_id="ABC12345",
    configuration_request_initiator="00",
    icc_data="...",
)

generated_message = reversal_response.generate_message()
print("Generated Reversal Response Message:")
print(generated_message)
