MANAGE = python manage.py
PROJECT_VERSION = 0.0.1

setup:
	@sudo apt-get install redis-server;
	@echo ">>>>>>> Creating virtual environment";
	@python3 -m venv venv; 
	@cat done.txt;


dev:
	pip install -r requirements.txt;
	$(MANAGE) makemigrations --merge;
	$(MANAGE) migrate;
	@cat done.txt;


run:
	$(MANAGE) runserver 0.0.0.0:8000;
