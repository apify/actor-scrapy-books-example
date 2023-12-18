.PHONY: clean install-dev lint type-check check-code format

DIRS_WITH_CODE = books_scraper

clean:
	rm -rf .venv .mypy_cache .pytest_cache .ruff_cache __pycache__

install-dev:
	python3.11 -m pip install --upgrade pip
	python3.11 -m pip install --no-interaction --no-ansi --no-cache-dir --requirement requirements.txt --requirement requirements-dev.txt
	pre-commit install

lint:
	ruff check $(DIRS_WITH_CODE)

type-check:
	mypy $(DIRS_WITH_CODE)

check-code: lint type-check

format:
	ruff check --fix $(DIRS_WITH_CODE)
	ruff format $(DIRS_WITH_CODE)
