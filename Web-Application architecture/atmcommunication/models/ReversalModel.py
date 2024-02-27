from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class MessageDelimiterEnum(str, Enum):
    PERIOD = "."


class SurchargeEnableFlagEnum(str, Enum):
    ENABLED = "1"
    DISABLED = "0"


class ReversalRequestMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as an Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric, host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=1, max_length=1, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    RequestType: str = Field(..., min_length=2, max_length=2, description="This two-character field identifies the type of request. Request Message contains an 86 in this field.", enum=["86"])
    LocalTransactionDate: str = Field(..., regex="[0-9]{8}", description="This fixed length field contains the six digit local date (MMDDYYYY), calculated by the authorization center using the time zone differential.")
    LocalTransactionTime: str = Field(..., regex="[0-9]{6}", description="This fixed length field contains the six digit local transaction time returned by the authorizing system (HHMMSS).")
    RetrievalReferenceNumber: str = Field(..., max_length=12, description="This fixed length field contains the twelve-character retrieval reference number returned by the authorizing system.")
    RequestedDollarAmount: str = Field(..., description="This field identifies the US dollar and US cents amounts entered at the keyboard.")
    DispensedDollarAmount: str = Field(..., description="This field identifies the US dollar amount dispensed by the terminal.")
    SurchargeAmount: str = Field(..., description="This field identifies the US dollar and US cents surcharge amount held locally within the terminal.")
    SurchargeEnableFlag: SurchargeEnableFlagEnum = Field(..., description="This field indicates whether or not the consumer was presented the surcharge screen and OKed the surcharge amount.")
    ICCData: str = Field(..., description="This field indicates the set of ICC related data.")
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")


class ReversalResponseMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as a Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric, host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=1, max_length=1, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    ResponseType: str = Field(..., min_length=2, max_length=2, description="This two-character field identifies the type of response. A Reversal Response Message contains an 86 in this field.", enum=["86"])
    ConfigurationRequestInitiator: str = Field(..., regex="[0-9]{2}", description="This two-digit field will cause the terminal to request configuration from the host processor.")
    ICCData: str = Field(..., description="This field indicates the set of ICC related data. Refer to Section 5 for detailed elements.")
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")
