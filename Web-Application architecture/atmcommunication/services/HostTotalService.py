from atmcommunication.models.AuthorizationModel import MessageDelimiterEnum
from atmcommunication.models.HostTotalModel import HostTotalsRequestMessageFields, HostTotalsResponseMessageFields

config_request_message = HostTotalsRequestMessageFields(
    ProtocolDependentHeader = "STX_Header",
    RecordFormat = "H",
    ApplicationType = "0",
    MessageDelimiterEnum = MessageDelimiterEnum.PERIOD,
    BankIDNumber = "1234567890",
    FieldSeparator = ":",
    TerminalID = "TERM01",
    RequestType = "87",
    ResetHostTotalsFlag = "1",
    ProtocolDependentTrailer = "ETX_Trailer",
)

config_response_message = HostTotalsResponseMessageFields(
    ProtocolDependentHeader = "STX_Header",
    RecordFormat = "H",
    ApplicationType = "0",
    MessageDelimiterEnum = MessageDelimiterEnum.PERIOD,
    BankIDNumber = "1234567890",
    FieldSeparator = ":",
    TerminalID = "TERM01",
    ResponseType = "87",
    NumberOfCashWithdrawals = "1234",
    NumberOfTransfers = "5678",
    NumberOfInquiries = "9012",
    NumberOfNonCashWithdrawals = "3456",
    TotalCashDispenseAmount = "12345678",
    TotalNonCashDispenseAmount = "87654321",
    TotalSurchargeAmount = "123456",
    ConfigurationRequestInitiator = "01",
    ProtocolDependentTrailer = "ETX_Trailer",
)


def getHostTotal(request: HostTotalsRequestMessageFields) -> HostTotalsResponseMessageFields:
    # Return a response
    response = HostTotalsResponseMessageFields(**request.dict())
    response.ResponseType = "88"  # Setting the ResponseType as "86" as per the specification
    return response
