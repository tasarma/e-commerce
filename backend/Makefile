.PHONY: install run migrate migrations migration superuser test update format add dry_run shell remove

PRP = poetry run python

install:
	poetry install

add:
	# Usage: make add arg=NAME_OF_THE_MODULE
	poetry add $(arg) 

remove:
	# Usage: make remove arg=NAME_OF_THE_MODULE
	poetry remove $(arg) 

run: 
	$(PRP) manage.py runserver 

migrate:
	$(PRP) manage.py migrate

migrations:
	$(PRP) manage.py makemigrations

migration:
	$(PRP) manage.py makemigrations $(app)

dry_run:
	# Display what the migration will actually look like 
	# without creating the migration file
	$(PRP) manage.py makemigrations --dry-run --verbosity 3

superuser:
	$(PRP) manage.py createsuperuser

test:
	poetry run pytest

update: 
	install migrate

format:
	pre-commit run --all-files

shell:
	$(PRP) manage.py shell