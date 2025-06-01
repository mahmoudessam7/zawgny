.PHONY: setup frontend

setup:
	@echo "Setting up project..."
	npm install

frontend:
	@echo "Starting frontend server..."
	npm run dev

dev:
	@echo "Starting development server..."
	npm run dev 