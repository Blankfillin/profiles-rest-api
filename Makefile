.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall
	poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: runserver
runserver:
	poetry run python -m core.manage runserver

.PHONY: migrations
migrations:
	poetry run python -m core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m core.manage migrate

.PHONY: flush
flush:
	poetry run python -m core.manage flush

.PHONY: superuser
superuser:
	poetry run python -m core.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit ;





drunserver:
	docker compose run web python manage.py runserver

dmigrations:
	docker compose run web python manage.py makemigrations

dmigrate:
	docker compose run web python manage.py migrate

dflush:
	docker compose run web python manage.py flush
