format:
	-poetry run docformatter -r --in-place --black core project || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black core project
	poetry run isort core project

lint: format
	poetry run flake8 core project
	poetry run pylint core project

test:
	poetry run python manage.py test

run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate 

migrations:
	poetry run python manage.py makemigrations 

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .pytest_cache/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +