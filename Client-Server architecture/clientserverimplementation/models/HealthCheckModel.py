class Message:
    def __init__(self, header, record_format, application_type, message_delimiter, bank_id, terminal_id, response_type, protocol_trailer):
        self.header = header
        self.record_format = record_format
        self.application_type = application_type
        self.message_delimiter = message_delimiter
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.response_type = response_type
        self.protocol_trailer = protocol_trailer

    def create_message(self):
        return (
            f"{self.header}{self.record_format}{self.application_type}"
            f"{self.message_delimiter}{self.bank_id}:{self.terminal_id}"
            f"{self.message_delimiter}{self.response_type}"
            f"{self.message_delimiter}{self.protocol_trailer}"
        )

class HealthCheck(Message):
    def __init__(self, bill_count_1, bill_count_2, bill_count_3=None, bill_count_4=None, mode_type=None, error_code=None, new_journal_count=None, header=None, record_format=None, application_type=None, message_delimiter=None, bank_id=None, terminal_id=None, response_type=None, protocol_trailer=None):
        self.bill_count_1 = bill_count_1
        self.bill_count_2 = bill_count_2
        self.bill_count_3 = bill_count_3
        self.bill_count_4 = bill_count_4
        self.mode_type = mode_type
        self.error_code = error_code
        self.new_journal_count = new_journal_count
        self.header = header
        self.record_format=record_format
        self.application_type=application_type
        self.message_delimiter=message_delimiter
        self.bank_id = bank_id
        self.terminal_id = terminal_id
        self.response_type = response_type
        self.protocol_trailer = protocol_trailer

    def create_health_check_message(self):
        message = super().create_message()
        bill_counts = f"{self.bill_count_1}{self.message_delimiter}{self.bill_count_2}"
        if self.bill_count_3:
            bill_counts += f"{self.message_delimiter}{self.bill_count_3}"
        if self.bill_count_4:
            bill_counts += f"{self.message_delimiter}{self.bill_count_4}"
        mode_type = f"{self.mode_type}" if self.mode_type else ""
        error_code = f"{self.error_code}" if self.error_code else ""
        journal_count = f"{self.new_journal_count}" if self.new_journal_count else ""
        return f"{message}{self.message_delimiter}{bill_counts}{mode_type}{error_code}{self.message_delimiter}{journal_count}{self.protocol_trailer}"

class HealthCheckConfirm(Message):
    def create_health_check_confirm_message(self):
        return super().create_message()

# Usage example:
health_check_msg = HealthCheck(
    bill_count_1="100",
    bill_count_2="200",
    bill_count_3="150",
    bill_count_4="180",
    mode_type="I",
    error_code="ERR123",
    new_journal_count="10"
)
print(health_check_msg.create_health_check_message())

health_check_confirm_msg = HealthCheckConfirm(header="Header",
    record_format="RecordFormat",
    application_type="ApplicationType",
    message_delimiter="MessageDelimiter",
    bank_id="BankID",
    terminal_id="TerminalID",
    response_type="ResponseType",
    protocol_trailer="ProtocolTrailer")
print(health_check_confirm_msg.create_health_check_confirm_message())
