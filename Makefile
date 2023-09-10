format:
	-poetry run docformatter -r --in-place --black src tests || [ $$? -eq 3 ] # accept error code 3 as success
	poetry run black src tests
	poetry run isort src tests

lint: format
	poetry run flake8 src tests
	poetry run pylint src

test:
	@bash -c 'poetry run pytest ; \
    EXIT_CODE=$$? ; \
    if [ -z "$$EXIT_CODE" ]; then exit 1 ; \
    elif [ $$EXIT_CODE -eq 5 ]; then exit 0 ; \
    else exit $$EXIT_CODE ; \
    fi'