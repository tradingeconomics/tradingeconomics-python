# Trading Economics Python SDK - Testing Guide

This guide explains how to run tests for the Trading Economics Python SDK. The test suite is organized into **unit tests** (fast, mocked) and **integration tests** (real API calls).

---

## Test Organization

```
tests/
├── archive/              # Legacy tests (deprecated)
├── integration/          # Integration tests (pytest, real API calls)
│   ├── conftest.py      # Pytest configuration and fixtures
│   ├── calendar/
│   ├── indicators/
│   ├── markets/
│   └── ...
├── calendar/            # Unit tests for calendar module
├── markets/             # Unit tests for markets module
├── indicators/          # Unit tests for indicators module
└── ...                  # Other module unit tests
```

---

## Unit Tests

**Purpose**: Fast, isolated tests that mock HTTP responses to validate SDK logic without hitting the real API.

**Technology**: `unittest` framework with mock responses

**No API key required**: Tests use mock data and don't consume API quota.

### Run All Unit Tests

From the project root:

```bash
python run_tests.py -v
```

This runs all unit tests sequentially by subdirectory, avoiding pandas circular import issues.

### Run Specific Module Tests

Run tests for a specific module:

```bash
# Calendar module tests
python -m unittest discover -s tests/calendar -v

# Markets module tests
python -m unittest discover -s tests/markets -v

# Indicators module tests
python -m unittest discover -s tests/indicators -v
```

### Run Single Test File

Run a specific test file:

```bash
python -m unittest tests.calendar.test_calendar_basic -v
```

### Run Single Test Class or Method

```bash
# Run specific test class
python -m unittest tests.calendar.test_calendar_basic.TestCalendarBasic -v

# Run specific test method
python -m unittest tests.calendar.test_calendar_basic.TestCalendarBasic.test_getCalendarData -v
```

---

## Integration Tests

**Purpose**: Validate API contract by making real HTTP requests to Trading Economics API.

**Technology**: `pytest` framework with real API calls

**API key required**: Uses `guest:guest` by default, or `apikey` environment variable for paid endpoints.

**Warning**: These tests consume API quota and require internet connectivity.

### Prerequisites

Install pytest (if not already installed):

```bash
pip install pytest pytest-mock
```

### Run All Integration Tests

From the project root:

```bash
pytest tests/integration/ -v
```

### Run Tests by Module

```bash
# Calendar integration tests
pytest tests/integration/calendar/ -v

# Indicators integration tests
pytest tests/integration/indicators/ -v

# Markets integration tests
pytest tests/integration/markets/ -v
```

### Run Tests by Marker

Integration tests use pytest markers for organization:

```bash
# Run only integration tests (excludes unit tests if mixed)
pytest -m integration -v

# Run slow tests (comprehensive API testing)
pytest -m slow -v

# Run tests requiring paid API subscription
pytest -m requires_paid_api -v

# Exclude slow tests for quick validation
pytest -m "not slow" -v
```

### Run Specific Test File

```bash
pytest tests/integration/calendar/test_calendar_basic.py -v
```

### Run Specific Test Class or Function

```bash
# Run specific test class
pytest tests/integration/calendar/test_calendar_basic.py::TestCalendarBasicFunctionality -v

# Run specific test function
pytest tests/integration/calendar/test_calendar_basic.py::TestCalendarBasicFunctionality::test_calendar_without_parameters -v
```

### Authentication for Integration Tests

Integration tests automatically authenticate using the `setup_api_credentials()` fixture in `conftest.py`:

1. **Default behavior**: Uses `guest:guest` credentials
2. **Custom API key**: Set environment variable before running tests:

```bash
# Windows PowerShell
$env:apikey = "your_api_key:your_api_secret"
pytest tests/integration/ -v

# Windows CMD
set apikey=your_api_key:your_api_secret
pytest tests/integration/ -v

# Linux/Mac
export apikey=your_api_key:your_api_secret
pytest tests/integration/ -v
```

---

## Useful Options

### Verbose Output

Add `-v` or `-vv` for more detailed output:

```bash
# Unit tests
python -m unittest discover -v

# Integration tests (more verbose)
pytest tests/integration/ -vv
```

### Stop on First Failure

```bash
# Unit tests
python -m unittest discover --failfast

# Integration tests
pytest tests/integration/ -x
```

### Show Print Statements

By default, pytest captures stdout. To see print statements:

```bash
pytest tests/integration/ -s
```

### Run Tests in Parallel (Integration only)

Install `pytest-xdist` for parallel execution:

```bash
pip install pytest-xdist
pytest tests/integration/ -n auto  # Use all CPU cores
pytest tests/integration/ -n 4     # Use 4 workers
```

**Warning**: Parallel tests may hit API rate limits.

### Generate Test Coverage Report

```bash
# Install coverage tools
pip install pytest-cov

# Run with coverage
pytest tests/integration/ --cov=tradingeconomics --cov-report=html

# Open htmlcov/index.html in browser to view report
```

---

## Quick Reference

| Task                        | Command                                            |
| --------------------------- | -------------------------------------------------- |
| All unit tests              | `python run_tests.py -v`                           |
| All integration tests       | `pytest tests/integration/ -v`                     |
| Calendar unit tests         | `python -m unittest discover -s tests/calendar -v` |
| Calendar integration tests  | `pytest tests/integration/calendar/ -v`            |
| Fast integration tests only | `pytest -m "not slow" tests/integration/ -v`       |
| Stop on first failure       | `pytest tests/integration/ -x`                     |
| Show print output           | `pytest tests/integration/ -s`                     |
| Custom API key              | `$env:apikey = "key:secret"` then run pytest       |

---

## Troubleshooting

### Circular Import Errors (Unit Tests)

If you see pandas circular import errors when running `unittest discover`, use `run_tests.py` instead:

```bash
python run_tests.py -v
```

### Authentication Errors (Integration Tests)

If integration tests fail with 401/403 errors:

1. Verify API key format: `user:password` or `apikey:apisecret`
2. Check environment variable: `echo $env:apikey` (PowerShell)
3. Ensure API key has required permissions for endpoints being tested

### Rate Limiting

If you get rate limit errors:

1. Add delays between test runs
2. Use paid API key with higher limits
3. Run fewer tests at once
4. Avoid parallel execution (`-n` flag)

### Network Errors

Integration tests require internet connectivity. If tests fail:

1. Check network connection
2. Verify API endpoint availability: https://api.tradingeconomics.com
3. Check firewall/proxy settings

---

## Legacy Tests

The `tests/archive/` directory contains deprecated integration tests using the old pattern. These tests are kept for reference but should not be used. See [archive/README.md](archive/README.md) for details.
