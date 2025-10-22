# Contributing to socketlock

We welcome contributions to socketlock! This document provides guidelines for contributing to the project.

## Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/socketlock.git
   cd socketlock
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

Run the test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=socketlock --cov-report=term-missing
```

## Code Style

We use the following tools to maintain code quality:

- **black** for code formatting
- **isort** for import sorting
- **mypy** for type checking
- **ruff** for linting

Format your code before committing:
```bash
black src tests
isort src tests
mypy src
```

## Making Changes

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and add tests
3. Ensure all tests pass
4. Commit your changes with a descriptive message
5. Push to your fork and create a pull request

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md with your changes under "Unreleased"
3. Ensure all tests pass and coverage is maintained
4. Your PR will be reviewed and merged once approved

## Reporting Issues

Please use GitHub Issues to report bugs or request features. Include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior

## License

By contributing to socketlock, you agree that your contributions will be licensed under the MIT License.