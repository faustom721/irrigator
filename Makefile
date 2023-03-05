MANAGE = python manage.py
PROJECT_VERSION = 0.0.1

setup:
	@sudo apt install python3.8-venv;
	@sudo apt install python-is-python3;
	@echo ">>>>>>> Creating virtual environment";
	@python -m venv venv; 
	@cat done.txt;


dev:
	@echo ">>>>>>> Installing dependencies";
	@pip install -r requirements.txt;
	$(MANAGE) makemigrations;
	$(MANAGE) migrate;
	@cat done.txt;


run:
	$(MANAGE) runserver 0.0.0.0:8000;
