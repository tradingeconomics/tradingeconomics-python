"""
Pytest configuration for integration tests.

These tests make REAL API calls to Trading Economics API.
- They are SLOW (network latency + API processing)
- They consume API quota
- They require valid API credentials

Usage:
    # Run all integration tests
    pytest tests/integration/ -v --tb=short

    # Run specific module
    pytest tests/integration/calendar/ -v

    # Run with markers
    pytest tests/integration/ -m "slow" -v
"""

import pytest
import os
import time
import tradingeconomics as te


@pytest.fixture(scope="session", autouse=True)
def setup_api_credentials():
    """
    Configure API credentials for integration tests.

    Reads from environment variable 'apikey' or uses guest credentials.
    Guest credentials have limited access and rate limits.
    """
    api_key = os.environ.get("apikey", "guest:guest")
    te.login(api_key)

    print(f"\n🔑 Using API key: {api_key[:10]}...")

    yield

    print("\n✅ Integration tests completed")


@pytest.fixture
def skip_if_no_api_key():
    """Skip test if using guest credentials (limited access)"""
    api_key = os.environ.get("apikey", "guest:guest")
    if api_key == "guest:guest":
        pytest.skip("Skipping: requires paid API key (guest has limited access)")


@pytest.fixture(autouse=True)
def throttle_api_requests():
    """
    Add delay between tests to respect API rate limits.

    This prevents:
    - HTTP 429 (Too Many Requests) errors
    - Temporary IP blocks from API server
    - Quota exhaustion with guest credentials

    The delay is applied AFTER each test completes.
    """
    yield  # Test runs here
    time.sleep(1)  # 1 second delay after each test


# Pytest markers for organizing tests
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line(
        "markers", "requires_paid_api: marks tests that require paid API access"
    )
