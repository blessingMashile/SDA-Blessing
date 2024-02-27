import socket
from clientserverimplementation.models import AuthorizationModel, ReversalModel, HostTotalModel, ConfigurationModel

HOST = 'localhost'  # Server's hostname or IP address
PORT = 12345        # Port used by the server

def send_request(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1026).decode('utf-8')
        print("Response:", response)

# Authorization Request
authorization_request_message = "AuthorizationRequestMessage:..."
send_request(AuthorizationModel.generated_message)

# Reversal Request
reversal_request_message = "ReversalRequestMessage:..."
send_request(ReversalModel.generated_message)

# Host Totals Request
host_totals_request_message = "HostTotalsRequestMessage:..."
send_request(HostTotalModel.generated_message)

# Configuration Request
configuration_request_message = "ConfigurationRequestMessage:..."
send_request(ConfigurationModel.configuration_request_message)

# Health Check
health_check_message = "HealthCheck:..."
send_request(health_check_message)
