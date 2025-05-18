.PHONY: setup frontend backend

setup:
	@echo "Setting up project..."
	npm install
	cd backend && chmod +x setup.sh && ./setup.sh

frontend:
	@echo "Starting frontend server..."
	npm run dev

backend:
	@echo "Starting backend server..."
	cd backend && source venv/bin/activate && python3 manage.py runserver 