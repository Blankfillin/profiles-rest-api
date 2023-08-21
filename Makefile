.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: runserver
runserver:
	poetry run python -m profiles_rest_api_core.manage runserver

.PHONY: migrations
migrations:
	poetry run python -m profiles_rest_api_core.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m profiles_rest_api_core.manage migrate

.PHONY: flush
flush:
	poetry run python -m profiles_rest_api_core.manage flush

.PHONY: shell
shell:
	poetry run python -m profiles_rest_api_core.manage shell

.PHONY: superuser
superuser:
	poetry run python -m profiles_rest_api_core.manage createsuperuser

.PHONY: update
update: install migrate install-pre-commit ;

.PHONY: db-up
db-up:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yml up --force-recreate db --detach

.PHONY: db-down
db-down:
	docker compose -f docker-compose.dev.yml down db

.PHONY: up
up: db-up migrations migrate runserver ;

.PHONY: down
down: db-down
