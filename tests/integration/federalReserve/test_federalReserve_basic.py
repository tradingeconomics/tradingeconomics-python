"""
Integration tests for Federal Reserve module.

Tests the following API calls with guest:guest credentials:
- te.getFedRStates()
- te.getFedRStates(county='arkansas')
- te.getFedRSnaps(country='united states')
- te.getFedRSnaps(symbol='ALLMARGATTN')
- te.getFedRSnaps(state='tennessee')
- te.getFedRCounty(state='arkansas')
- te.getFedRCounty(county='Pike County, AR')
- te.getFedRSnaps(url='/united-states/all-marginally-attached-workers-for-tennessee-fed-data.html')
- te.getFedRHistorical(symbol='racedisparity005007')
- te.getFedRHistorical(symbol=['racedisparity005007', '2020ratio002013'])
- te.getFedRHistorical(symbol='BAMLC0A1CAAAEY', initDate='2017-05-01')
- te.getFedRHistorical(symbol='BAMLC0A1CAAAEY', initDate='2017-05-01', endDate='2019-01-01')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time
from functools import wraps


# Configure API access
te.login("guest:guest")


def retry_on_server_error(max_retries=3, delay=2):
    """Decorator to retry test on HTTP 500 errors (server-side issues)."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except te.functions.WebRequestError as e:
                    if "500" in str(e) and attempt < max_retries - 1:
                        print(
                            f"\n⚠️  Server error (attempt {attempt + 1}/{max_retries}), retrying in {delay}s..."
                        )
                        time.sleep(delay)
                        continue
                    raise
            return None

        return wrapper

    return decorator


class TestFedRStates:
    """Test Federal Reserve states endpoints."""

    def test_states_all(self):
        """Test: te.getFedRStates()"""
        result = te.getFedRStates()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure of first item
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_states_county_arkansas(self):
        """Test: te.getFedRStates(county='arkansas')"""
        result = te.getFedRStates(county="arkansas")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFedRSnaps:
    """Test Federal Reserve snapshots endpoints."""

    def tearDown(self):
        """Add delay between tests to avoid API rate limiting."""
        time.sleep(2)

    def test_snaps_country_united_states(self):
        """Test: te.getFedRSnaps(country='united states')"""
        result = te.getFedRSnaps(country="united states")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_snaps_symbol_allmargattn(self):
        """Test: te.getFedRSnaps(symbol='ALLMARGATTN')"""
        result = te.getFedRSnaps(symbol="ALLMARGATTN")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_snaps_state_tennessee(self):
        """Test: te.getFedRSnaps(state='tennessee')"""
        result = te.getFedRSnaps(state="tennessee")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    @retry_on_server_error(max_retries=3, delay=3)
    def test_snaps_url(self):
        """Test: te.getFedRSnaps(url='/united-states/all-marginally-attached-workers-for-tennessee-fed-data.html')

        Note: This endpoint occasionally returns HTTP 500 errors due to server-side issues.
        The test includes retry logic to handle transient failures.
        """
        result = te.getFedRSnaps(
            url="/united-states/all-marginally-attached-workers-for-tennessee-fed-data.html"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFedRCounty:
    """Test Federal Reserve county endpoints."""

    def test_county_state_arkansas(self):
        """Test: te.getFedRCounty(state='arkansas')"""
        result = te.getFedRCounty(state="arkansas")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_county_pike_county_ar(self):
        """Test: te.getFedRCounty(county='Pike County, AR')"""
        result = te.getFedRCounty(county="Pike County, AR")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFedRHistorical:
    """Test Federal Reserve historical data endpoints."""

    def test_historical_single_symbol(self):
        """Test: te.getFedRHistorical(symbol='racedisparity005007')"""
        result = te.getFedRHistorical(symbol="racedisparity005007")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)
        # Historical data should have date field
        keys = [k.lower() for k in first_item.keys()]
        assert any(key in ["date", "datetime"] for key in keys)

    def test_historical_multiple_symbols(self):
        """Test: te.getFedRHistorical(symbol=['racedisparity005007', '2020ratio002013'])"""
        result = te.getFedRHistorical(symbol=["racedisparity005007", "2020ratio002013"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_with_init_date(self):
        """Test: te.getFedRHistorical(symbol='BAMLC0A1CAAAEY', initDate='2017-05-01')"""
        result = te.getFedRHistorical(symbol="BAMLC0A1CAAAEY", initDate="2017-05-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_with_date_range(self):
        """Test: te.getFedRHistorical(symbol='BAMLC0A1CAAAEY', initDate='2017-05-01', endDate='2019-01-01')"""
        result = te.getFedRHistorical(
            symbol="BAMLC0A1CAAAEY", initDate="2017-05-01", endDate="2019-01-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFedROutputFormats:
    """Test different output formats."""

    def test_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getFedRStates(output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getFedRStates(output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_output_format_raw(self):
        """Test raw output format."""
        result = te.getFedRStates(output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

    def test_historical_output_format_df(self):
        """Test DataFrame output for historical data."""
        result = te.getFedRHistorical(symbol="racedisparity005007", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
