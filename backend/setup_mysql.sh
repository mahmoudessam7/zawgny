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

# Check if MySQL is installed
if ! command -v mysql &> /dev/null; then
    echo -e "${RED}MySQL is not installed. Please install it first.${NC}"
    echo -e "${YELLOW}You can install it with: brew install mysql${NC}"
    exit 1
fi

# Get database connection details
echo -e "${GREEN}Setting up MySQL database for Zawgny...${NC}"
read -p "Enter MySQL database name (default: zawgny): " DB_NAME
DB_NAME=${DB_NAME:-zawgny}
read -p "Enter MySQL username: " DB_USER
read -p "Enter MySQL password: " DB_PASSWORD
read -p "Enter MySQL host (default: localhost): " DB_HOST
DB_HOST=${DB_HOST:-localhost}
read -p "Enter MySQL port (default: 3306): " DB_PORT
DB_PORT=${DB_PORT:-3306}

# Create settings_local.py with MySQL config
echo -e "${BLUE}Creating local settings file...${NC}"
cat > zawgny_project/settings_local.py << EOF
# MySQL database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${DB_NAME}',
        'USER': '${DB_USER}',
        'PASSWORD': '${DB_PASSWORD}',
        'HOST': '${DB_HOST}',
        'PORT': '${DB_PORT}',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
EOF

# Update settings.py to import local settings if not already done
if ! grep -q "settings_local" zawgny_project/settings.py; then
    echo -e "\n# Import local settings if they exist\ntry:\n    from .settings_local import *\nexcept ImportError:\n    pass" >> zawgny_project/settings.py
fi

# Install MySQL client for Python
echo -e "${BLUE}Installing MySQL adapter for Python...${NC}"
pip install mysqlclient
pip freeze > requirements.txt

# Create database if it doesn't exist
echo -e "${BLUE}Creating MySQL database...${NC}"
mysql -h"$DB_HOST" -P"$DB_PORT" -u"$DB_USER" -p"$DB_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Run migrations
echo -e "${BLUE}Running migrations...${NC}"
python3 manage.py makemigrations
python3 manage.py migrate

# Create a superuser
echo -e "${BLUE}Creating a superuser for admin access...${NC}"
python3 manage.py createsuperuser

echo -e "${GREEN}MySQL database setup complete!${NC}"
echo -e "${YELLOW}You can now run the server with: python3 manage.py runserver${NC}"
echo -e "${GREEN}Connect to MySQL in Sequel Ace with:${NC}"
echo -e "Host: ${DB_HOST}"
echo -e "Port: ${DB_PORT}"
echo -e "Username: ${DB_USER}" 
echo -e "Password: (your password)"
echo -e "Database: ${DB_NAME}" 