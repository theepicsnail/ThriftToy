#!/bin/bash
echo "Starting server:"
python server.py &
SERVER_PID=$!
echo "Server started."

sleep .1 #Give the server some time to start up

echo ""
echo "Running the client (Should not find key)"
python client.py
echo "Client finished."

echo ""
echo "Running the client a 2nd time (Finds key)"
python client.py
echo "Client finished."

kill $SERVER_PID
