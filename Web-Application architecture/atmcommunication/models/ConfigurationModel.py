from typing import List
from enum import Enum
from pydantic import BaseModel, Field


class MessageDelimiterEnum(str, Enum):
    PERIOD = "."


class AIDInformationEnum(str, Enum):
    R = "R"
    A = "A"
    D = "D"


class ConfigurationRequestMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as a Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=3, max_length=3, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    RequestType: str = Field(..., min_length=2, max_length=2, description="This two character field identifies the type of request. A Configuration Request Message contains an 88 in this field.", enum=["88"])
    UnknownValueField: str = Field(..., description="Unknown value. Not used.")
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")


class ConfigurationResponseMessageFields(BaseModel):
    ProtocolDependentHeader: str = Field(..., max_length=255, description="Protocol uses this header on all transmitted message formats. This field contains one or more protocol characters and precedes the message text. This header typically includes the start-of-text (STX) character.")
    RecordFormat: str = Field(..., min_length=1, max_length=1, description="This one character field identifies this message as an Spark ATM formatted POS message.", enum=["H"])
    ApplicationType: str = Field(..., min_length=1, max_length=1, description="This one character field must contain an ASCII zero.", enum=["0"])
    MessageDelimiter: MessageDelimiterEnum = Field(MessageDelimiterEnum.PERIOD, description="The message delimiter separates the format and application type designators from the body of the message. The message delimiter is defined as a period.")
    BankIDNumber: str = Field(..., max_length=255, description="This fixed length field contains the alphanumeric host processor assigned. Bank Identification Number (BIN).")
    FieldSeparator: str = Field(..., min_length=3, max_length=3, description="This one character field is used as a separator between various fields in the message.", enum=[":1C"])
    TerminalID: str = Field(..., max_length=8, description="This fixed length field contains the 8 character Terminal ID assigned by the host processor. This field is used to identify a specific terminal. This field must be unique across all terminals within a single host processor.")
    ResponseType: str = Field(..., min_length=2, max_length=2, description="This two character field identifies the type of response. A Configuration Response Message contains an 88 in this field.", enum=["88"])
    LocalDate: str = Field(..., max_length=8, description="This fixed length field contains the eight digit local date (MMDDYYYY) calculated by the authorization center using the time zone differential.")
    LocalTime: str = Field(..., max_length=6, description="This fixed length field contains the six digit local transaction time returned by the authorizing system (HHMMSS).")
    HealthMessageTimerValue: str = Field(..., description="Not Used")
    TDESWorkingKeyPart1: str = Field(..., max_length=16, description="This fixed length field contains the first 16 chars of the new 32 character working Key encrypted with the terminal's Master key.")
    SurchargeAmount: str = Field(..., description="This variable length field contains the current per transaction US dollar and US cents surcharge amount within the terminal.")
    BINListEnableFlag: str = Field(..., description="Not Used")
    TDESWorkingKeyPart2: str = Field(..., max_length=16, description="This fixed length field contains the second 16 chars of the new 32 character working Key encrypted with the terminal's Master key.")
    TDESWorkingKeyPart1Repeated: str = Field(..., max_length=16, description="This fixed length field contains the first 16 chars of the new 32 character working Key encrypted with the terminal's Master key. This is a repeat of the first TDES Working Key Part 1 above.")
    AIDInformation: AIDInformationEnum = Field(..., description="This field indicates the action to be performed for the list of AIDs on Terminal.")
    AIDList: str = Field(..., description="Fields from ASI to AID repeated as many as Number of AIDs.")
    CAPublicKeyInformation: AIDInformationEnum = Field(..., description="This field indicates the action to be performed for the list of CA Public Keys on Terminal.")
    CAPublicKeyList: str = Field(..., description="Fields from RID to Check Sum repeated as many as Number of Keys.")
    ProtocolDependentTrailer: str = Field(..., max_length=255, description="The variable-length Protocol Dependent Trailer field indicates the end of the message.")

