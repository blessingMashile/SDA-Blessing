from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class MessageDelimiterEnum(str, Enum):
    PERIOD = "."


class HostTotalsRequestMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as an Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=1, max_length=1, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    RequestType: str = Field(..., min_length=2, max_length=2, description="This two character field identifies the type of request. Request Message contains an 87 in this field.", enum=["87"])
    ResetHostTotalsFlag: str = Field(..., min_length=1, max_length=1, description="This one character field contains the host totals reset flag. A 0 means don't reset the host totals and a 1 means reset the host totals.", enum=["0", "1"])
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")


class HostTotalsResponseMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as an Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=1, max_length=1, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    ResponseType: str = Field(..., min_length=2, max_length=2, description="This two character field identifies the type of response. A Host Totals Response Message contains an 87 in this field.", enum=["87"])
    NumberOfCashWithdrawals: str = Field(..., min_length=4, max_length=4, description="This fixed length field contains the total number of cash withdrawals performed at this terminal since the last time the totals were reset. The number will range from 0000 to 9999.")
    NumberOfTransfers: str = Field(..., min_length=4, max_length=4, description="This fixed length field contains the total number of transfers performed at this terminal since the last time the totals were reset. The number will range from 0000 to 9999.")
    NumberOfInquiries: str = Field(..., min_length=4, max_length=4, description="This fixed length field contains the total number of inquiries performed at this terminal since the last time the totals were reset. The number will range from 0000 to 9999.")
    NumberOfNonCashWithdrawals: str = Field(..., min_length=4, max_length=4, description="This fixed length field contains the total number of non-cash, valued item withdrawals performed at this terminal since the last time the totals were reset. The number will range from 0000 to 9999.")
    TotalCashDispenseAmount: str = Field(..., min_length=6, max_length=8, description="This variable length field contains the total US dollar and US cents amount dispensed by this terminal since the last time the totals were reset. The data is in the following format: ddddddcc The US cents field will always be present even if zero.")
    TotalNonCashDispenseAmount: str = Field(..., min_length=6, max_length=8, description="This variable length field contains the total value (in US dollar and US cents) of non-cash, valued items dispensed by this terminal since the last time the totals were reset. The data is in the following formats: ddddddcc The US cent field will always be present even if zero.")
    TotalSurchargeAmount: str = Field(..., min_length=5, max_length=6, description="This variable length field contains the total US dollar and US cents surcharge amount at this terminal since the last time the totals were reset. The data is in the following format: ddddcc The US cents field will always be present even if zero.")
    ConfigurationRequestInitiator: str = Field(..., min_length=2, max_length=2, description="This two digit field will cause the terminal to request configuration from the host processor. A value of 0 I in this field will cause the terminal to send a Configuration Request Message to the host processor. An empty field or a value of 00 will not cause a Configuration Request Message to be sent. Any other value will be ignored.")
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")
