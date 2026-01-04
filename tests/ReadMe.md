# Test Suite Overview

This folder contains the full automated test suite for the shared models package.
Tests are grouped by domain and mirror the structure under `src/`.

## Test layout

- `tests/generic_models/`: Tests for generic response, pagination, and errors.
- `tests/userverse_models/`: Tests for user, company, and related domain models.
- `tests/validators/`: Tests for shared validators (for example, phone numbers).

## Run the full test suite

From the project root:

```bash
source .venv/bin/activate
pytest
```

If you use `uv` to manage the virtual environment:

```bash
uv venv
source .venv/bin/activate
uv sync
pytest
```

## Run a subset

Run a specific folder:

```bash
pytest tests/validators
```

Run a single file:

```bash
pytest tests/userverse_models/test_user.py
```

## Notes

- Pytest is configured to include `src` on the import path via `pyproject.toml`.
- If you see import errors, verify the virtual environment is active and dependencies are installed.
