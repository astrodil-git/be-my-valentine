#!/bin/bash
# Start a simple HTTP server on an available port (avoids "Address already in use")
cd "$(dirname "$0")"
PORT=$(python3 -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
port = s.getsockname()[1]
s.close()
print(port)
")
echo "Serving at http://localhost:$PORT — open in your browser"
python3 -m http.server "$PORT"
