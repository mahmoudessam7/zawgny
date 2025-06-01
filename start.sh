#!/bin/bash

# Exit on error
set -e

# Colors for better output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Zawgny application...${NC}"

# Start the frontend server
echo -e "${GREEN}Starting frontend development server...${NC}"
npm run dev

echo -e "${GREEN}Frontend server running at http://localhost:5173/${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop the server${NC}" 