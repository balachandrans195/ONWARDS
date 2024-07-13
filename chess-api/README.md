This project provides an API endpoint to determine valid moves for a given chess piece on a chessboard.

### Docker

1. Build the Docker image:

    ```sh
    docker build -t chess-api .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8000:8000 chess-api
    ```

### Local Development

1. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:

    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## Usage

The API endpoint follows the format: `http://localhost:8000/chess/<slug>`

