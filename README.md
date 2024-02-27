# Server-Client System with SQLite Database

This is a simple server-client system implemented in Python that communicates with an SQLite database. The server provides health and configuration information to clients upon request.

There are 2 implementations, mainly using client server architecture and the other a web application.

## Requirements

- Python 3.x
- SQLite3

## Usage

1. **Setting up the SQLite Database:**

    - Ensure you have SQLite installed on your system.
    - Run the following commands in your terminal or command prompt to create the SQLite database file `config.db` and populate it with example data:

    ```bash
    sqlite3 config.db
    ```

    ```sql
    CREATE TABLE configuration (
        id INTEGER PRIMARY KEY,
        setting TEXT
    );

    INSERT INTO configuration (setting) VALUES ('Example setting 1');
    INSERT INTO configuration (setting) VALUES ('Example setting 2');
    INSERT INTO configuration (setting) VALUES ('Example setting 3');

    .quit
    ```

2. **Running the Server:**

    - Open a terminal or command prompt and navigate to the project directory.
    - Run the following command to start the server:

    ```bash
    python server.py
    ```

3. **Running the Client:**

    - Open another terminal or command prompt and navigate to the project directory.
    - Run the following command to start the client:

    ```bash
    python client.py
    ```

    - The client will send requests to the server to fetch health and configuration information, and display the responses.

## Files

- `server.py`: Python script implementing the server that communicates with the SQLite database.
- `client.py`: Python script implementing the client to interact with the server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
