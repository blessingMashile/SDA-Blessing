from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class MessageDelimiterEnum(str, Enum):
    PERIOD = "."


class HealthCheckMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as a Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="This message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric, host processor assigned. Bank Identification Number (BIN).")
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    ResponseType: str = Field(..., min_length=2, max_length=2, description="This two character field identifies the type of response. A Health Check Message contains an H0 in this field.", enum=["H0"])
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="This variable-length Protocol Dependent Trailer field indicates the end of the message.")


class HealthCheckConfirmMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as a Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="This message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric, host processor assigned. Bank Identification Number (BIN).")
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    ResponseType: str = Field(..., min_length=2, max_length=2, description="This two characters field identifies the type of response. A Health Check Confirm Message contains an H0 in this field.", enum=["H0"])
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="This variable-length Protocol Dependent Trailer field indicates the end of the message.")
