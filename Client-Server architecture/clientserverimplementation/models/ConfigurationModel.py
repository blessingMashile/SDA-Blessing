#Configuration server
class ConfigurationRequestMessage:
    def __init__(self, message):
        self.message = message

    def parse_message(self):
        fields = self.message.split(":")
        if len(fields) < 7:
            return None  # Invalid message format

        protocol_dependent_header = fields[0]
        record_format = fields[1]
        application_type = fields[2]
        bank_id = fields[3]
        terminal_id = fields[4]
        request_type = fields[5]
        unknown_value_field = fields[6]
        protocol_dependent_trailer = fields[7]

        return {
            "protocol_dependent_header": protocol_dependent_header,
            "record_format": record_format,
            "application_type": application_type,
            "bank_id": bank_id,
            "terminal_id": terminal_id,
            "request_type": request_type,
            "unknown_value_field": unknown_value_field,
            "protocol_dependent_trailer": protocol_dependent_trailer,
        }


#Usage
configuration_request_message = "H0.123456:ABC12345:88:3."

parsed_message = ConfigurationRequestMessage(configuration_request_message).parse_message()
print("Parsed Configuration Request Message:")
print(parsed_message)
