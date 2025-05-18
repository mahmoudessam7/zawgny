# Zawgny Backend (Django)

This is the backend API for the Zawgny matrimonial site, built with Django and Django REST Framework.

## Setup

1. Create a virtual environment:
```
python3 -m venv venv
```

2. Activate the virtual environment:
```
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install django djangorestframework django-cors-headers Pillow
```

4. Apply migrations:
```
python manage.py migrate
```

5. Create a superuser (admin):
```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

The API will be available at http://localhost:8000/api/

## API Endpoints

### Authentication
- `POST /api/register/` - Register a new user
- `POST /api/login/` - Login and get token

### Profiles
- `GET /api/profiles/` - List all profiles (admin only)
- `GET /api/profiles/my_profile/` - Get current user's profile
- `PATCH /api/profiles/{id}/` - Update a profile
- `GET /api/profiles/potential_matches/` - Get potential matches

### Match Preferences
- `GET /api/preferences/` - Get current user's preferences
- `POST /api/preferences/` - Create preferences
- `PATCH /api/preferences/{id}/` - Update preferences

### Match Requests
- `GET /api/match-requests/` - Get current user's match requests
- `POST /api/match-requests/` - Send a match request
- `POST /api/match-requests/{id}/accept/` - Accept a match request
- `POST /api/match-requests/{id}/reject/` - Reject a match request

### Conversations
- `GET /api/conversations/` - Get current user's conversations

### Messages
- `GET /api/messages/?conversation={id}` - Get messages in a conversation
- `POST /api/messages/` - Send a message

## Models

### Profile
- User information including personal details, education, religiosity, etc.

### MatchPreference
- User's preferences for matching (age range, height, education, etc.)

### MatchRequest
- Request from one user to another for matching

### Conversation
- Chat conversation between matched users

### Message
- Individual messages within a conversation

## Admin Interface

The Django admin interface is available at http://localhost:8000/admin/ and provides access to:
- User management
- Profile verification
- Match request moderation
- Conversation monitoring

## Frontend Integration

This backend is designed to work with the Vue.js frontend located in the `zawgny` directory. 