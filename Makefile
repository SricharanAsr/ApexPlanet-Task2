# Makefile for ApexPlanet-Task2

.PHONY: help install setup run test clean

help:
	@echo "Usage:"
	@echo "  make install  - Install Python dependencies"
	@echo "  make setup    - Generate synthetic data and initialize database"
	@echo "  make run      - Run Exploratory Data Analysis"
	@echo "  make test     - Run unit tests"
	@echo "  make clean    - Remove generated data and temporary files"

install:
	pip install -r requirements.txt

setup:
	python setup_data.py

run:
	python eda_analysis.py

test:
	pytest tests/

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -f sales_data.csv
	rm -f sales_database.db
	rm -f summary_statistics.csv
	rm -f sql_results.txt
	rm -rf plots/
