# Zawgny - Technical Documentation

## Overview
Zawgny is a Vue.js Islamic matrimonial website designed to help Muslim individuals find suitable marriage partners according to Islamic principles. The application features user profiles, matching preferences, and a modern responsive interface with Arabic language support.

## Project Architecture

### Frontend (Vue.js)
- Single Page Application built with Vue 3 Composition API
- State management using Pinia
- Routing with Vue Router
- Styling with Tailwind CSS
- Data persistence using browser localStorage
- Internationalization support

## Technology Stack

### Frontend Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| Vue.js | 3.x | Frontend framework |
| Tailwind CSS | 3.3.3 | Utility-first CSS framework |
| Pinia | Latest | State management |
| Vue Router | Latest | Client-side routing |
| Vite | Latest | Build tool and development server |

## Setup Instructions

### Prerequisites
- Node.js (v16+)
- npm or yarn
- Git

### Quick Start (Recommended)
The project includes a start script for running the development server:

```bash
# Clone the repository
git clone https://github.com/mahmoudessam7/zawgny.git
cd zawgny

# Make the start script executable
chmod +x start.sh

# Run the development server
./start.sh
```

This will start the frontend development server at http://localhost:5173.

### Setup with Make
The project includes a Makefile for setup and running the development server:

```bash
# Clone the repository
git clone https://github.com/mahmoudessam7/zawgny.git
cd zawgny

# Run the setup script (installs dependencies)
make setup

# Start the development server
make dev
```

### Manual Setup

```bash
# From the project root
npm install
npm run dev
```
The application will run on http://localhost:5173

## Development Workflow

### Frontend Development
The frontend is a Vue 3 application with the following structure:
- `src/components/` - Reusable UI components
- `src/views/` - Page components
- `src/stores/` - Pinia state stores
- `src/router/` - Route definitions
- `src/assets/` - Static assets

To add a new feature:
1. Create necessary components in `src/components/`
2. Add new views if needed in `src/views/`
3. Update the router in `src/router/`
4. Add state management in `src/stores/` if needed

### Data Storage
The application uses browser localStorage for data persistence:
- User authentication state
- Profile information
- Match preferences
- Mock potential matches data

## Application Features

### Current Features
- User registration and authentication (localStorage-based)
- Profile creation and management
- Match preferences specification
- Viewing potential matches (mock data)
- Responsive design with Arabic language support
- Modern UI with Tailwind CSS

### State Management
The application uses Pinia stores for:
- `auth.js` - User authentication and session management
- `profile.js` - User profiles, preferences, and potential matches
- `counter.js` - Example counter store

## Deployment

### Frontend Deployment
1. Build the production version: `npm run build`
2. The output will be in the `dist/` directory
3. Deploy these static files to your web hosting service (Netlify, Vercel, etc.)

### Environment Configuration
The application is configured for development by default. For production:
1. Update any hardcoded URLs if needed
2. Configure proper error handling
3. Optimize build settings in `vite.config.js`

## Troubleshooting

### Common Issues

1. **Development server not starting**
   - Ensure Node.js 16+ is installed
   - Clear node_modules: `rm -rf node_modules`
   - Reinstall dependencies: `npm install`

2. **Build issues**
   - Check for TypeScript/JavaScript errors
   - Verify all imports are correct
   - Run `npm run build` to check for build errors

3. **Styling issues**
   - Verify Tailwind CSS is properly configured
   - Check `tailwind.config.js` for custom configurations
   - Ensure PostCSS is working correctly

## Project Structure

```
zawgny/
├── src/
│   ├── components/     # Reusable Vue components
│   ├── views/         # Page components
│   ├── stores/        # Pinia state stores
│   ├── router/        # Vue Router configuration
│   ├── assets/        # Static assets
│   ├── App.vue        # Root component
│   └── main.js        # Application entry point
├── public/            # Public static files
├── package.json       # Dependencies and scripts
├── vite.config.js     # Vite configuration
├── tailwind.config.js # Tailwind CSS configuration
├── Makefile          # Build and development commands
├── start.sh          # Quick start script
└── README.md         # Project documentation
``` 