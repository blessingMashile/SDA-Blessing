import sqlite3


def checkArrayLength(fields, index):
    if index > len(fields):
        return 
    else:
        return fields[index]

#Host totals
class HostTotalsRequestMessage:
    def __init__(self, bank_id, terminal_id, reset_host_totals_flag):
        self.protocol_dependent_header = ""
        self.record_format = "H"
        self.application_type = "0"
        self.message_delimiter = "."
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.request_type = "87"
        self.reset_host_totals_flag = reset_host_totals_flag
        self.protocol_dependent_trailer = ""

    def generate_message(self):
        message = (
            f"{self.protocol_dependent_header}{self.record_format}{self.application_type}"
            f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}:{self.request_type}:"
            f"{self.reset_host_totals_flag}{self.protocol_dependent_trailer}"
        )
        return message


# Example usage
host_totals_request = HostTotalsRequestMessage(
    bank_id="123456",
    terminal_id="ABC12345",
    reset_host_totals_flag="0",  # 0 means don't reset, 1 means reset
)

generated_message = host_totals_request.generate_message()
print("Generated Host Totals Request Message:")
print(generated_message)

class HostTotalsResponseMessage:
    def __init__(self, message):
        self.message = message

    def parse_message(self):
        # Connect to SQLite database
        conn = sqlite3.connect('host_total_requests.db')
        cursor = conn.cursor()

        # Search for authorization response in database
        cursor.execute('''SELECT * FROM host_total_requests WHERE transaction_sequence_number = ?''',
                    (host_totals_request.terminal_id,))
        data = cursor.fetchone()

        # Close the database connection
        conn.close()
        
        if data:
            fields = self.message.split(":")
            if len(fields) < 10:
                return None  # Invalid message format

            protocol_dependent_header = fields[0]
            record_format = fields[1]
            application_type = fields[2]
            bank_id = fields[3]
            terminal_id = fields[4]
            response_type = fields[5]
            num_cash_withdrawals = fields[6]
            num_transfers = fields[7]
            num_inquiries = fields[8]
            num_non_cash_withdrawals = fields[9]
            total_cash_dispense_amount = fields[10]
            total_non_cash_dispense_amount = checkArrayLength(fields, 11)
            total_surcharge_amount = checkArrayLength(fields, 11)
            configuration_request_initiator = checkArrayLength(fields, 11)
            protocol_dependent_trailer = checkArrayLength(fields, 11)

            return {
                "protocol_dependent_header": protocol_dependent_header,
                "record_format": record_format,
                "application_type": application_type,
                "bank_id": bank_id,
                "terminal_id": terminal_id,
                "response_type": response_type,
                "num_cash_withdrawals": num_cash_withdrawals,
                "num_transfers": num_transfers,
                "num_inquiries": num_inquiries,
                "num_non_cash_withdrawals": num_non_cash_withdrawals,
                "total_cash_dispense_amount": total_cash_dispense_amount,
                "total_non_cash_dispense_amount": total_non_cash_dispense_amount,
                "total_surcharge_amount": total_surcharge_amount,
                "configuration_request_initiator": configuration_request_initiator,
                "protocol_dependent_trailer": protocol_dependent_trailer,
            }


# Example usage
host_totals_response_message = "H0.123456:ABC12345:87:1234:5678:0002:0034:0123:0076:0000001250:0000000050:0000000100:00."

parsed_message = HostTotalsResponseMessage(host_totals_response_message).parse_message()
print("Parsed Host Totals Response Message:")
print(parsed_message)
