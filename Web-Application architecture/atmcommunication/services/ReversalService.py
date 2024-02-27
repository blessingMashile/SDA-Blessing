from atmcommunication.models.AuthorizationModel import MessageDelimiterEnum
from atmcommunication.models.ReversalModel import ReversalRequestMessageFields, ReversalResponseMessageFields, SurchargeEnableFlagEnum


example_reversal_request = ReversalRequestMessageFields(
    ProtocolDependentHeader="STX12345ETX",
    RecordFormat="H",
    ApplicationType="0",
    MessageDelimiter=MessageDelimiterEnum.PERIOD,
    BankIDNumber="123456789",
    FieldSeparator=":",
    TerminalID="12345678",
    RequestType="86",
    LocalTransactionDate="01252024",
    LocalTransactionTime="235959",
    RetrievalReferenceNumber="123456789012",
    RequestedDollarAmount="100.00",
    DispensedDollarAmount="100.00",
    SurchargeAmount="0.00",
    SurchargeEnableFlag=SurchargeEnableFlagEnum.DISABLED,
    ICCData="ICC data goes here",
    ProtocolDependentTrailer="Trailer"
)

example_reversal_response = ReversalResponseMessageFields(
    ProtocolDependentHeader="STX54321ETX",
    RecordFormat="H",
    ApplicationType="0",
    MessageDelimiter=MessageDelimiterEnum.PERIOD,
    BankIDNumber="987654321",
    FieldSeparator=":",
    TerminalID="87654321",
    ResponseType="86",
    ConfigurationRequestInitiator="01",
    ICCData="ICC data goes here",
    ProtocolDependentTrailer="Trailer"
)

def requestReversal(request: ReversalRequestMessageFields) -> ReversalResponseMessageFields:
    # Return a response
    response = ReversalResponseMessageFields(**request.dict())
    response.ResponseType = "86"  # Setting the ResponseType as "86" as per the specification
    return response
