#!/bin/bash

# Exit on error
set -e

# Colors for better output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Zawgny application...${NC}"

# Start the backend server using make backend in background
echo -e "${GREEN}Starting backend server...${NC}"
make backend &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2
echo -e "${GREEN}Backend server running at http://localhost:8000/${NC}"

# Start the frontend server using make frontend
echo -e "${GREEN}Starting frontend server...${NC}"
make frontend &
FRONTEND_PID=$!

echo -e "${GREEN}Frontend server running at http://localhost:5173/${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop both servers${NC}"

# Function to kill both processes on exit
cleanup() {
    echo -e "\n${GREEN}Shutting down servers...${NC}"
    kill $BACKEND_PID
    kill $FRONTEND_PID
    exit 0
}

# Register the cleanup function for SIGINT and SIGTERM signals
trap cleanup SIGINT SIGTERM

# Keep the script running until ctrl+c
wait 