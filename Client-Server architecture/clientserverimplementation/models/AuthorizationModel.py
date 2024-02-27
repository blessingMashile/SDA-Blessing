#Authorization server
import sqlite3


class AuthorizationRequestMessage:
    def __init__(self, bank_id, terminal_id, operation_code, source_account, destination_account,
                 transaction_sequence_number, track_1_data, track_2_data, track_3_data, pin_buffer,
                 transaction_amount, surcharge_amount, surcharge_enable_flag, icc_data):
        self.protocol_dependent_header = ""
        self.record_format = "H"
        self.application_type = "0"
        self.message_delimiter = "."
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.request_type = "85"
        self.operation_code = operation_code
        self.source_account = source_account
        self.destination_account = destination_account
        self.transaction_sequence_number = transaction_sequence_number
        self.track_1_data = track_1_data
        self.track_2_data = track_2_data
        self.track_3_data = track_3_data
        self.pin_buffer = pin_buffer
        self.transaction_amount = transaction_amount
        self.surcharge_amount = surcharge_amount
        self.surcharge_enable_flag = surcharge_enable_flag
        self.icc_data = icc_data
        self.protocol_dependent_trailer = ""

    def generate_message(self):
        message = (
            f"{self.protocol_dependent_header}{self.record_format}{self.application_type}"
            f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}:{self.request_type}:"
            f"{self.operation_code}:{self.source_account}:{self.destination_account}:"
            f"{self.transaction_sequence_number}:{self.track_1_data}:{self.track_2_data}:"
            f"{self.track_3_data}:{self.pin_buffer}:{self.transaction_amount}:{self.surcharge_amount}:"
            f"{self.surcharge_enable_flag}:{self.icc_data}{self.protocol_dependent_trailer}"
        )
        return message


# Example usage
authorization_request = AuthorizationRequestMessage(
    bank_id="123456",
    terminal_id="ABC12345",
    operation_code="CW",
    source_account="CA",
    destination_account="SA",
    transaction_sequence_number="0001",
    track_1_data="...",
    track_2_data="...",
    track_3_data="...",
    pin_buffer="1234567890123456",
    transaction_amount="10000",
    surcharge_amount="100",
    surcharge_enable_flag="1",
    icc_data="...",
)

generated_message = authorization_request.generate_message()
print("Generated Authorization Request Message:")
print(generated_message)

class AuthorizationResponseMessage:
    def __init__(self, bank_id, terminal_id, transaction_sequence_number, response_code,
                 local_transaction_date, local_transaction_time, retrieval_reference_number,
                 system_trace_audit_number, network_id_code, settlement_date, account_balance,
                 available_balance, surcharge_amount, authorization_response_text,
                 configuration_request_initiator, icc_data):
        self.protocol_dependent_header = ""
        self.record_format = "H"
        self.application_type = "0"
        self.message_delimiter = "."
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.response_type = "85"
        self.transaction_sequence_number = transaction_sequence_number
        self.response_code = response_code
        self.local_transaction_date = local_transaction_date
        self.local_transaction_time = local_transaction_time
        self.retrieval_reference_number = retrieval_reference_number
        self.system_trace_audit_number = system_trace_audit_number
        self.network_id_code = network_id_code
        self.settlement_date = settlement_date
        self.account_balance = account_balance
        self.available_balance = available_balance
        self.surcharge_amount = surcharge_amount
        self.authorization_response_text = authorization_response_text
        self.configuration_request_initiator = configuration_request_initiator
        self.icc_data = icc_data
        self.protocol_dependent_trailer = ""

    def generate_message(self):
        # Connect to SQLite database
        conn = sqlite3.connect('authorization_requests.db')
        cursor = conn.cursor()

        # Search for authorization response in database
        cursor.execute('''SELECT * FROM authorization_request WHERE transaction_sequence_number = ?''',
                    (authorization_request.transaction_sequence_number,))
        data = cursor.fetchone()

        # Close the database connection
        conn.close()
        
        if data:
            message = (
                f"{self.protocol_dependent_header}{self.record_format}{self.application_type}"
                f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}:{self.response_type}:"
                f"{self.transaction_sequence_number}:{self.response_code}:{self.local_transaction_date}:"
                f"{self.local_transaction_time}:{self.retrieval_reference_number}:{self.system_trace_audit_number}:"
                f"{self.network_id_code}:{self.settlement_date}:{self.account_balance}:{self.available_balance}:"
                f"{self.surcharge_amount}:{self.authorization_response_text}:"
                f"{self.configuration_request_initiator}:{self.icc_data}{self.protocol_dependent_trailer}"
            )
        return message


# Example usage
authorization_response = AuthorizationResponseMessage(
    bank_id="123456",
    terminal_id="ABC12345",
    transaction_sequence_number="0001",
    response_code="00",
    local_transaction_date="01012022",
    local_transaction_time="123456",
    retrieval_reference_number="123456789012",
    system_trace_audit_number="654321",
    network_id_code="01",
    settlement_date="01012022",
    account_balance="10000",
    available_balance="10000",
    surcharge_amount="0",
    authorization_response_text="Approved",
    configuration_request_initiator="00",
    icc_data="...",
)

generated_message = authorization_response.generate_message()
print("Generated Authorization Response Message:")
print(generated_message)
