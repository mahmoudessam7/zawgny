# Zawgny - Islamic Matrimonial Site

A full-stack matrimonial site built with Vue.js and Django, designed to help Muslim individuals find suitable marriage partners according to Islamic principles.

## Project Structure

The project is organized as follows:
- `/` - Vue.js frontend (root directory)
- `/backend` - Django REST API backend

## Frontend Setup

1. Install dependencies:
```
npm install
```

2. Run development server:
```
npm run dev
```

The frontend will be available at http://localhost:5173

## Backend Setup

1. Change to the backend directory:
```
cd backend
```

2. Run the setup script:
```
./setup.sh
```

3. Activate the virtual environment and run the server:
```
source venv/bin/activate
python3 manage.py runserver
```

The API will be available at http://localhost:8000/api/

## Features

- User registration and authentication
- Profile creation and management
- Match preferences specification
- Finding potential matches
- Sending and responding to match requests
- Secure messaging between matched users
- Admin moderation and verification

## Development

To work on this project:

1. Start the backend server in one terminal
2. Start the frontend server in another terminal
3. Both will communicate via the API endpoints

## API Endpoints

See `/backend/README.md` for detailed API documentation.

## Technologies Used

- **Frontend**: Vue 3, Tailwind CSS, Pinia
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production)
