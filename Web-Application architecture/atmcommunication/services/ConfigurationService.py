from atmcommunication.models.AuthorizationModel import MessageDelimiterEnum
from atmcommunication.models.ConfigurationModel import AIDInformationEnum, ConfigurationRequestMessageFields, ConfigurationResponseMessageFields

config_request_message = ConfigurationRequestMessageFields(
    ProtocolDependentHeader="Header123",
    RecordFormat="H",
    ApplicationType="0",
    MessageDelimiter=MessageDelimiterEnum.PERIOD,
    BankIDNumber="1234567890",
    FieldSeparator=":1C",
    TerminalID="T1234567",
    RequestType="88",
    UnknownValueField="Unknown",
    ProtocolDependentTrailer="Trailer123"
)

config_response_message = ConfigurationResponseMessageFields(
    ProtocolDependentHeader="Header123",
    RecordFormat="H",
    ApplicationType="0",
    MessageDelimiter=MessageDelimiterEnum.PERIOD,
    BankIDNumber="1234567890",
    FieldSeparator=":1C",
    TerminalID="T1234567",
    ResponseType="88",
    LocalDate="02012024",
    LocalTime="235959",
    HealthMessageTimerValue="Not Used",
    TDESWorkingKeyPart1="KeyPart1",
    SurchargeAmount="1.50",
    BINListEnableFlag="Not Used",
    TDESWorkingKeyPart2="KeyPart2",
    TDESWorkingKeyPart1Repeated="KeyPart1",
    AIDInformation=AIDInformationEnum.R,
    AIDList="AIDList",
    CAPublicKeyInformation=AIDInformationEnum.A,
    CAPublicKeyList="CAPublicKeyList",
    ProtocolDependentTrailer="Trailer123"
)


def getConfiguration(request: ConfigurationRequestMessageFields) -> ConfigurationResponseMessageFields:
    # Return a response
    response = ConfigurationResponseMessageFields(**request.dict())
    response.ResponseType = "88"  # Setting the ResponseType as "86" as per the specification
    return response
