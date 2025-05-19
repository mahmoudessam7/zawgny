#!/bin/bash

# Colors for better output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if virtual environment exists and activate it
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Creating one...${NC}"
    python3 -m venv venv
fi

source venv/bin/activate

# Make sure dependencies are installed
pip install -r requirements.txt

# Function to setup SQLite (development)
setup_sqlite() {
    echo -e "${GREEN}Setting up SQLite database...${NC}"
    
    # Run migrations
    echo -e "${BLUE}Running migrations...${NC}"
    python3 manage.py makemigrations
    python3 manage.py migrate
    
    # Create a superuser
    echo -e "${BLUE}Creating a superuser for admin access...${NC}"
    python3 manage.py createsuperuser
    
    echo -e "${GREEN}SQLite database setup complete!${NC}"
    echo -e "${YELLOW}You can now run the server with: python3 manage.py runserver${NC}"
}

# Function to setup PostgreSQL (production)
setup_postgres() {
    echo -e "${GREEN}Setting up PostgreSQL database...${NC}"
    
    # Check if PostgreSQL is installed
    if ! command -v psql &> /dev/null; then
        echo -e "${RED}PostgreSQL is not installed. Please install it first.${NC}"
        exit 1
    fi
    
    # Get database connection details
    read -p "Enter PostgreSQL database name: " DB_NAME
    read -p "Enter PostgreSQL username: " DB_USER
    read -p "Enter PostgreSQL password: " DB_PASSWORD
    read -p "Enter PostgreSQL host (default: localhost): " DB_HOST
    DB_HOST=${DB_HOST:-localhost}
    read -p "Enter PostgreSQL port (default: 5432): " DB_PORT
    DB_PORT=${DB_PORT:-5432}
    
    # Create settings_local.py with PostgreSQL config
    echo -e "${BLUE}Creating local settings file...${NC}"
    cat > zawgny_project/settings_local.py << EOF
# PostgreSQL database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '${DB_NAME}',
        'USER': '${DB_USER}',
        'PASSWORD': '${DB_PASSWORD}',
        'HOST': '${DB_HOST}',
        'PORT': '${DB_PORT}',
    }
}
EOF
    
    # Update settings.py to import local settings
    if ! grep -q "settings_local" zawgny_project/settings.py; then
        echo -e "\n# Import local settings if they exist\ntry:\n    from .settings_local import *\nexcept ImportError:\n    pass" >> zawgny_project/settings.py
    fi
    
    # Install psycopg2
    echo -e "${BLUE}Installing PostgreSQL adapter for Python...${NC}"
    pip install psycopg2-binary
    pip freeze > requirements.txt
    
    # Run migrations
    echo -e "${BLUE}Running migrations...${NC}"
    python3 manage.py makemigrations
    python3 manage.py migrate
    
    # Create a superuser
    echo -e "${BLUE}Creating a superuser for admin access...${NC}"
    python3 manage.py createsuperuser
    
    echo -e "${GREEN}PostgreSQL database setup complete!${NC}"
    echo -e "${YELLOW}You can now run the server with: python3 manage.py runserver${NC}"
}

# Main menu
echo -e "${GREEN}Zawgny Database Setup${NC}"
echo -e "${YELLOW}Choose a database option:${NC}"
echo "1) SQLite (for development)"
echo "2) PostgreSQL (for production)"
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        setup_sqlite
        ;;
    2)
        setup_postgres
        ;;
    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac 