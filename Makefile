POETRY = poetry
DEV_IMAGE = $(APP_NAME):dev
PROD_IMAGE = $(APP_NAME):prod
PORT ?= 8000
ENV_FILE ?= .env

.PHONY: install lock lint check test precommit ci-local

install:
	$(POETRY) install

lock:
	$(POETRY) lock

lint:
	$(POETRY) run ruff check --fix .

check:
	$(POETRY) run ruff check .
	$(POETRY) run mypy me_ai

test:
	$(POETRY) run pytest -q

precommit:
	PRE_COMMIT_HOME=.pre-commit-cache $(POETRY) run pre-commit run --all-files

ci-local: install lock lint check test

.PHONY: compose-up compose-down compose-logs compose-ps

compose-up:
	docker compose --profile all up -d --build

compose-down:
	docker compose --profile all down -v

compose-logs:
	docker compose --profile all logs -f

compose-ps:
	docker compose --profile all ps
