from atmcommunication.models.HealthCheckModel import HealthCheckConfirmMessageFields, HealthCheckMessageFields


health_check_request = HealthCheckMessageFields(
    ProtocolDependentHeader="Example Header",
    RecordFormat="H",
    ApplicationType="0",
    MessageDelimiter=".",
    BankIDNumber="1234567890",
    TerminalID="TERMIN01",
    ResponseType="H0",
    ProtocolDependentTrailer="Example Trailer"
)

health_check_response = HealthCheckConfirmMessageFields(
    ProtocolDependentHeader=health_check_request.ProtocolDependentHeader,
    RecordFormat=health_check_request.RecordFormat,
    ApplicationType=health_check_request.ApplicationType,
    MessageDelimiter=health_check_request.MessageDelimiter,
    BankIDNumber=health_check_request.BankIDNumber,
    TerminalID=health_check_request.TerminalID,
    ResponseType="H0",  # Set ResponseType as "H0" as per the specification
    ProtocolDependentTrailer=health_check_request.ProtocolDependentTrailer
)

def perform_health_check(request: HealthCheckMessageFields) -> HealthCheckConfirmMessageFields:
    # Return a response
    response = HealthCheckConfirmMessageFields(**request.dict())
    response.ResponseType = "H0"  # Setting the ResponseType as "H0" as per the specification
    return response
