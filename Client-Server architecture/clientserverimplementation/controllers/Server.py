import socket

from atmcommunication.models import HealthCheckModel
from clientserverimplementation.models import AuthorizationModel, ReversalModel, HostTotalModel, ConfigurationModel

# Server settings
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345  # Port to listen on

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for incoming connections

def main():
    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        
        client_data = client_socket.recv(1024).decode("utf-8")

        # Parse client message and determine its type
        if "AuthorizationRequestMessage" in client_data:
            # Handle Authorization Request Message
            authorization_request = AuthorizationModel.AuthorizationRequestMessage(...)  
            generated_message = authorization_request.generate_message()  
            print("Generated Authorization Request Message:")
            print(generated_message)
            client_socket.sendall(generated_message.encode("utf-8"))

        elif "ReversalRequestMessage" in client_data:
            # Handle Reversal Request Message
            reversal_request = ReversalModel.ReversalRequestMessage(...)  
            generated_message = reversal_request.generate_message()  
            print("Generated Reversal Request Message:")
            print(generated_message)
            client_socket.sendall(generated_message.encode("utf-8"))

        elif "HostTotalsRequestMessage" in client_data:
            # Handle Host Totals Request Message
            host_totals_request = HostTotalModel.HostTotalsRequestMessage(...)  
            generated_message = host_totals_request.generate_message()  
            print("Generated Host Totals Request Message:")
            print(generated_message)
            client_socket.sendall(generated_message.encode("utf-8"))

        elif "ConfigurationRequestMessage" in client_data:
            # Handle Configuration Request Message
            configuration_request = ConfigurationModel.ConfigurationRequestMessage(...)  
            generated_message = configuration_request.parse_message()  
            print("Generated Configuration Request Message:")
            print(generated_message)
            client_socket.sendall(generated_message.encode("utf-8"))

        elif "HealthCheck" in client_data:
            # Handle Health Check Message
            health_check_message = HealthCheckModel(...)  
            generated_message = health_check_message.create_health_check_message()  
            print("Generated Health Check Message:")
            print(generated_message)
            client_socket.sendall(generated_message.encode("utf-8"))

        else:
            print("Unknown message type received.")

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    main()
