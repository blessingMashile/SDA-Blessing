from atmcommunication.models.AuthorizationModel import AuthorizationRequestMessageFields
from atmcommunication.models.ReversalModel import ReversalRequestMessageFields
from atmcommunication.models.ConfigurationModel import ConfigurationRequestMessageFields
from atmcommunication.models.HostTotalModel import HostTotalsRequestMessageFields
from atmcommunication.services.ReversalService import requestReversal
from atmcommunication.services.ConfigurationService import getConfiguration
from atmcommunication.services.HostTotalService import getHostTotal
from flask import Flask, jsonify, request
from atmcommunication.services.AuthorizationService import getAccessToken, validateToken
from atmcommunication.services.HealthCheckService import perform_health_check

from atmcommunication.models.HealthCheckModel import HealthCheckMessageFields
from flask import Flask, request 
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
from jsonschema import ValidationError

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secret key of your choice
jwt = JWTManager(app)

@app.route('/health_check', methods=['POST'])
async def health_check(request: HealthCheckMessageFields):
    return perform_health_check(request)

# Route to generate access token
@app.route('/get_access_token', methods=['POST'])
async def get_access_token():
    try:
        request_data = request.json
        authorization_request = AuthorizationRequestMessageFields(**request_data)

        return getAccessToken(authorization_request)
    except ValidationError as e:
        # Handle validation errors
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500
    
@app.route('/validate_token', methods=['POST'])
@jwt_required()
async def validate_token():
    return validateToken(get_jwt_identity())

# Add reversal request
@app.route('/reversal', methods=['POST'])
@jwt_required()
async def request_reversal(request: ReversalRequestMessageFields):
    return requestReversal(request)

# Add host total request
@app.route('/host_total', methods=['POST'])
@jwt_required()
async def host_total(request: HostTotalsRequestMessageFields):
    return getHostTotal(request)

# Add configuration request -> change banks/ server config in DB
@app.route('/configuration', methods=['POST'])
@jwt_required()
async def get_configuration(request: ConfigurationRequestMessageFields):
    return getConfiguration(request)

if __name__ == '__main__':
    app.run(debug=True)
