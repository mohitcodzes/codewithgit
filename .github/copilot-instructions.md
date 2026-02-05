# Copilot Instructions for codewithgit

This document provides guidance for AI coding agents working on this Python project.

## Project Overview

This is a Python development project. The codebase is currently in initialization phase with a standard Python project structure.

## Architecture & Structure

- **Source Code**: Python modules in root or `src/` directory (to be established)
- **Configuration**: Standard Python project files (`setup.py`, `pyproject.toml`, `requirements.txt`, `setup.cfg`)
- **Tests**: Test modules following naming convention (typically `test_*.py` or `*_test.py`)
- **Documentation**: Markdown files in project root or `docs/` directory

## Development Workflows

### Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools
```

### Running Tests
- Use `pytest` for test execution: `pytest` or `pytest tests/`
- Coverage reports: `pytest --cov=src`
- Verbose output: `pytest -v`

### Code Quality
- **Linting**: `flake8 src/` or `pylint src/`
- **Formatting**: `black src/`
- **Type Checking**: `mypy src/`
- **Pre-commit**: Configure pre-commit hooks for consistent code quality

## Project Conventions

### Code Style
- Follow PEP 8 standards
- Use Black for code formatting (consistent with `pyproject.toml` settings)
- Use type hints for function arguments and return types
- Docstrings: Google or NumPy style (specify which as project grows)

### Module Organization
- Group related functionality into modules
- Use clear, descriptive names for functions and classes
- Keep functions focused and reasonably sized

### Testing
- Write unit tests for all public functions
- Use pytest fixtures for test setup
- Organize tests by module they test

## Key Files & Patterns

| File/Directory | Purpose |
|---|---|
| `requirements.txt` | Production dependencies |
| `requirements-dev.txt` | Development & testing dependencies |
| `setup.py` or `pyproject.toml` | Project metadata & configuration |
| `.gitignore` | Standard Python ignores configured |

## Integration Points

*To be documented as dependencies and integrations are added to the project*

---

**Last Updated**: January 18, 2026  
**Status**: Template for new Python project

When project files are added, update this document with specific patterns, key architectural decisions, and important workflows.
