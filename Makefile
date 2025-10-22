.PHONY: help install dev test clean build upload

help:
	@echo "Available commands:"
	@echo "  make install    - Install the package"
	@echo "  make dev        - Install in development mode with dev dependencies"
	@echo "  make test       - Run tests"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make build      - Build distribution packages"
	@echo "  make upload     - Upload to PyPI (requires credentials)"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	PYTHONPATH=src pytest tests/ -v

clean:
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".*.lock" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*