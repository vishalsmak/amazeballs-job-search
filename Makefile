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
	sh docker-entry.sh

docker-build:
	docker-compose build
	docker tag amazeballs-job-search_job_search:latest europe-west2-docker.pkg.dev/qmul-346622/qmul/job_search:latest

docker: docker-build
	docker-compose up

create-kube:
	gcloud container clusters get-credentials qmul --region europe-west2 --project qmul-346622
	kubectl create deployment qmul --image=europe-west2-docker.pkg.dev/qmul-346622/qmul/job_search:latest
	kubectl scale deployment qmul --replicas=2
	kubectl autoscale deployment qmul --cpu-percent=80 --min=1 --max=5
	kubectl expose deployment qmul --name=job-search --type=LoadBalancer --port 80 --target-port 5000
	kubectl get service

update-kube: docker-build
	docker push europe-west2-docker.pkg.dev/qmul-346622/qmul/job_search:latest
	kubectl set image deployment/qmul job-search-f6scv=europe-west2-docker.pkg.dev/qmul-346622/qmul/job_search:latest
