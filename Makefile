.PHONY: setup serve build deploy sync

setup:
	pip install -r requirements-docs.txt

serve:
	mkdocs serve

build:
	mkdocs build

deploy:
	mkdocs gh-deploy --force

sync:
	python3 scripts/sync_activities.py
	python3 scripts/generate_charts.py
