# Zawgny - Technical Documentation

## Overview
Zawgny is a full-stack Islamic matrimonial website designed to help Muslim individuals find suitable marriage partners according to Islamic principles. The application features user profiles, matching algorithms, communication tools, and admin moderation.

## Project Architecture

### Frontend (Vue.js)
- Single Page Application built with Vue 3 Composition API
- State management using Pinia
- Routing with Vue Router
- Styling with Tailwind CSS
- Internationalization support

### Backend (Django)
- RESTful API built with Django and Django REST Framework
- Token-based authentication
- SQLite database (development) / PostgreSQL (production)
- Media file handling with Pillow

## Technology Stack

### Frontend Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| Vue.js | 3.x | Frontend framework |
| Tailwind CSS | 3.3.3 | Utility-first CSS framework |
| Pinia | Latest | State management |
| Vue Router | Latest | Client-side routing |
| Axios | Latest | HTTP client for API requests |

### Backend Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| Django | 5.2.1 | Web framework |
| Django REST Framework | 3.16.0 | API development |
| django-cors-headers | 4.7.0 | Handle CORS |
| Pillow | 11.2.1 | Image processing |

## Setup Instructions

### Prerequisites
- Node.js (v16+)
- npm or yarn
- Python 3.10+
- Git

### Quick Start (Recommended)
The project includes a start script for running both frontend and backend simultaneously:

```bash
# Clone the repository
git clone https://github.com/mahmoudessam7/zawgny.git
cd zawgny

# Make the start script executable
chmod +x start.sh

# Run both frontend and backend with a single command
./start.sh
```

This will start both the frontend (http://localhost:5173) and backend (http://localhost:8000) servers in the same terminal window. Press Ctrl+C to stop both servers.

### Setup with Make
The project includes a Makefile for setup and running individual services:

```bash
# Clone the repository
git clone https://github.com/mahmoudessam7/zawgny.git
cd zawgny

# Run the setup script (installs both frontend and backend dependencies)
make setup

# Start the frontend server
make frontend

# In a separate terminal, start the backend server
make backend
```

### Manual Setup

#### Frontend Setup
```bash
# From the project root
npm install
npm run dev
```
The frontend will run on http://localhost:5173

#### Backend Setup
```bash
# From the project root
cd backend
chmod +x setup.sh
./setup.sh
source venv/bin/activate
python3 manage.py runserver
```
The backend API will run on http://localhost:8000/api/

## Development Workflow

### Frontend Development
The frontend is a Vue 3 application with the following structure:
- `src/components/` - Reusable UI components
- `src/views/` - Page components
- `src/stores/` - Pinia state stores
- `src/services/` - API service interfaces
- `src/router/` - Route definitions
- `src/assets/` - Static assets

To add a new feature:
1. Create necessary components in `src/components/`
2. Add new views if needed in `src/views/`
3. Update the router in `src/router/`
4. Add any API services in `src/services/`

### Backend Development
The backend is a Django application with:
- `api/` - Main Django app with models, views, and serializers
- `zawgny_project/` - Django project settings

Key models include:
- User authentication (Django's built-in User)
- Profile
- MatchPreference
- MatchRequest
- Conversation
- Message

API endpoints are defined using Django REST Framework and follow RESTful principles.

## API Documentation

The backend provides the following RESTful API endpoints:

### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Authenticate user and get token

### Profiles
- `GET /api/profiles/my_profile/` - Get current user's profile
- `PATCH /api/profiles/:id/` - Update a profile
- `GET /api/profiles/potential_matches/` - Get potential matches

### Match Preferences
- `GET /api/preferences/` - Get user's match preferences
- `POST /api/preferences/` - Create match preferences
- `PATCH /api/preferences/:id/` - Update match preferences

### Match Requests
- `GET /api/match-requests/` - List user's match requests
- `POST /api/match-requests/` - Send a match request
- `POST /api/match-requests/:id/accept/` - Accept a match request
- `POST /api/match-requests/:id/reject/` - Reject a match request

### Messaging
- `GET /api/conversations/` - List user's conversations
- `GET /api/messages/?conversation=:id` - Get messages for a conversation
- `POST /api/messages/` - Send a new message

## Deployment

### Frontend Deployment
1. Build the production version: `npm run build`
2. The output will be in the `dist/` directory
3. Deploy these static files to your web hosting service

### Backend Deployment
1. Configure production settings in `zawgny_project/settings.py`
2. Set up a PostgreSQL database
3. Configure environment variables for sensitive information
4. Deploy to a server using Gunicorn and Nginx

## Troubleshooting

### Common Issues

1. **Backend server not starting**
   - Ensure Python 3.10+ is installed
   - Try using `python3` instead of `python` commands
   - Check virtual environment is activated

2. **Frontend build issues**
   - Clear node_modules: `rm -rf node_modules`
   - Reinstall dependencies: `npm install`

3. **CORS errors**
   - Verify CORS settings in Django settings.py
   - Check the API_URL in the frontend configuration 