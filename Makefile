VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: setup serve build deploy sync venv

venv:
	python3 -m venv $(VENV)

setup: venv
	$(PIP) install -r requirements-docs.txt

serve:
	$(VENV)/bin/mkdocs serve

build:
	$(VENV)/bin/mkdocs build

deploy:
	$(VENV)/bin/mkdocs gh-deploy --force

sync:
	$(PYTHON) scripts/sync_activities.py
	$(PYTHON) scripts/generate_charts.py
