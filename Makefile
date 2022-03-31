SHELL := /bin/bash

env-setup:
	rm -rf venv
	# Python 3.9.12
	python3.9 -m venv venv; \
	source venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt

pre-commit-mac:
	brew install pre-commit
	pre-commit install
	pre-commit run --all-files
