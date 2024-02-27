from atmcommunication.models.AuthorizationModel import AuthorizationRequestMessageFields, AuthorizationResponseMessageFields, MessageDelimiterEnum
from flask import jsonify

from atmcommunication.services.UserService import verify_user

def getAccessToken(authorization_request: AuthorizationRequestMessageFields):
    if(authorization_request.BankIDNumber is None):
        return jsonify({'message': 'Invalid bank Id', 'authRequest': authorization_request}), 400

    authorization_response = AuthorizationResponseMessageFields(
            ProtocolDependentHeader="Sample Header",
            RecordFormat="H",
            ApplicationType="0",
            MessageDelimiter=MessageDelimiterEnum.PERIOD,
            BankIDNumber="Sample Bank ID",
            FieldSeparator=":1C",
            TerminalID="Sample Terminal ID",
            ResponseType="85",
            TransactionSequenceNumber="1234",
            ResponseCode="00",
            LocalTransactionDate="220226",
            LocalTransactionTime="235959",
            RetrievalReferenceNumber="123456789012",
            SystemTraceAuditNumber="123456",
            NetworkIDCode="NA",
            SettlementDate="2202",
            AccountBalance="100.00",
            AvailableBalance="100.00",
            SurchargeAmount="0.00",
            AuthorizationResponseText="Sample Authorization Response",
            ConfigurationRequestInitiator="NA",
            ICCData="Sample ICC Data",
            ProtocolDependentTrailer="Sample Trailer"
        )
    return jsonify(authorization_response.dict())
    
def validateToken(current_user):
    return jsonify({'message': 'Token is valid', 'user': current_user}), 200
