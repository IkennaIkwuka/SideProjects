#!/bin/bash

# Run pytest with coverage report for the src directory and main.py
# --cov=. tells it to track everything in the current folder
# --cov-report term-missing shows the specific line numbers not covered
pytest --cov=. --cov-report term-missing