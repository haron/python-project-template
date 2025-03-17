.DEFAULT_GOAL := deploy
SHELL := /usr/bin/env -S bash -O globstar # makes work globs like **/*.py
HOST ?= {{ cookiecutter.deploy_host }}
PROJECT ?= {{ cookiecutter.project_slug }}
ENV ?= prod
SLUG := $(PROJECT)-$(ENV)
PREFIX := /var/www/$(SLUG)
USER := {{ cookiecutter.deploy_user }}
ANSIBLE := ansible-playbook deploy.yml -i $(HOST), -e project=$(PROJECT) -u $(USER)
SSH := ssh -t $(USER)@$(HOST)

deploy: linter
	uv sync
	$(ANSIBLE) --skip-tags=full

init: clean
	uv venv -q
	uv sync

clean:
	rm -rf .venv db.sqlite3 **/__pycache__

linter: githook
	python -m py_compile **/*.py
	uvx isort -q **/*.py
	uvx ruff format -q --line-length 140 **/*.py
	uvx ruff check -q --ignore F401 **/*.py

githook:
	uvx pre-commit install > /dev/null

safety:
	uv tool run safety scan -o bare

full-deploy:
	uv sync
	$(ANSIBLE)

logs:
	ssh -t $(HOST) less +GF /var/log/supervisor/$(SLUG).log

migrate:
	./manage.py makemigrations db
	$(SSH) rm -rf $(PREFIX)/db/migrations
	make deploy
	$(SSH) uv run --directory $(PREFIX) manage.py migrate

restart:
	$(ANSIBLE) --tags restart
