.PHONY: clean install-dev lint type-check check-code format

clean:
	rm -rf .venv .mypy_cache .pytest_cache .ruff_cache __pycache__ storage

install-dev:
	uv sync --all-extras

lint:
	uv run ruff format --check
	uv run ruff check

type-check:
	uv run mypy

check-code: lint type-check

format:
	uv run ruff check --fix
	uv run ruff format
