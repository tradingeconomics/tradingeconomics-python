# Archived Legacy Tests

This directory contains legacy integration tests that were previously located in the root of the `tests/` directory.

## About These Tests

These tests use the old naming convention (`_test_*.py`) and are **integration tests** that make real HTTP requests to the Trading Economics API.

### Files:

- `_test_calendar.py` - Calendar endpoint integration tests
- `_test_credit_ratings.py` - Credit ratings endpoint integration tests
- `_test_dividends.py` - Dividends endpoint integration tests
- `_test_forecasts.py` - Forecasts endpoint integration tests
- `_test_indicators.py` - Indicators endpoint integration tests
- `_test_ipo.py` - IPO endpoint integration tests
- `_test_stockSplits.py` - Stock splits endpoint integration tests

### Characteristics:

- Use `unittest` framework
- Make real API calls with `guest:guest` credentials
- Compare SDK output against direct API requests
- Global `te.login('guest:guest')` at file level

### Why Archived?

These tests have been superseded by:

- **Unit tests** in module-specific directories (`tests/calendar/`, `tests/markets/`, etc.) that use mocks
- **Integration tests** in `tests/integration/` that use pytest framework

### Running These Tests

If you need to run these legacy tests:

```bash
# Run all archived tests
python -m unittest discover -s tests/archive -v

# Run specific test file
python -m unittest tests.archive._test_calendar -v
```

**Note:** These tests consume API quota and require network connectivity.

### Future

These tests may be removed in a future version once all functionality is covered by modern unit/integration tests.
