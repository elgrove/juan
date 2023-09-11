format:
	-poetry run docformatter -r --in-place --black core project || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black core project
	poetry run isort core project

lint: format
	poetry run flake8 core project
	poetry run pylint core project

test:
	@bash -c 'poetry run pytest ; \
    EXIT_CODE=$$? ; \
    if [ -z "$$EXIT_CODE" ]; then exit 1 ; \
    elif [ $$EXIT_CODE -eq 5 ]; then exit 0 ; \
    else exit $$EXIT_CODE ; \
    fi'

run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate 

migrations:
	poetry run python manage.py makemigrations 