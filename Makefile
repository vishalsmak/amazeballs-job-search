SHELL := /bin/bash

env-setup:
	rm -rf venv
	# Python 3.9.12
	python3.9 -m venv venv; \
	source venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	python3 pre_requisites.py

pre-commit-mac:
	brew install pre-commit
	pre-commit install
	pre-commit run --all-files

local:
	source venv/bin/activate; \
	export CONFIG_PATH=configs/local.cfg; \
	export FLASK_APP=app/server; \
	export FLASK_ENV=development; \
	docker-compose -f docker-compose.local.yaml up -d; \
	flask run

cloud:
	source venv/bin/activate; \
	export CONFIG_PATH=configs/cloud.cfg; \
	export FLASK_APP=app/server; \
	export FLASK_ENV=development; \
	flask run
