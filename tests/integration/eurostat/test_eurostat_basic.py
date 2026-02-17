"""
Integration tests for Eurostat module.

Tests the following API calls with guest:guest credentials:
- te.getEurostatData(lists='countries')
- te.getEurostatData(lists='categories')
- te.getEurostatData(symbol='51640')
- te.getEurostatData(category_group='Poverty')
- te.getEurostatData(category='People at risk of income poverty after social transfers')
- te.getEurostatData(country='Denmark')
- te.getEurostatData(country='Denmark', category_group='Interest rates')
- te.getEurostatData(country='European Union', category='Harmonised unemployment rate: Females')
- te.getHistoricalEurostat(ID='24804')
- te.getHistoricalEurostat(ID='24804', initDate='2015-01-01')
- te.getHistoricalEurostat(ID='24804', initDate='2016-01-01', endDate='2020-01-01')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time


# Configure API access
te.login("guest:guest")


class TestEurostatLists:
    """Test Eurostat list endpoints."""

    def test_lists_countries(self):
        """Test: te.getEurostatData(lists='countries')"""
        result = te.getEurostatData(lists="countries")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure of first item
        first_item = result[0]
        assert isinstance(first_item, dict)
        assert "country" in first_item or "Country" in first_item

    def test_lists_categories(self):
        """Test: te.getEurostatData(lists='categories')"""
        result = te.getEurostatData(lists="categories")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure of first item
        first_item = result[0]
        assert isinstance(first_item, dict)
        # Categories should have category or category_group fields
        keys = first_item.keys()
        assert any(
            key.lower() in ["category", "category_group", "categorygroup"]
            for key in keys
        )


class TestEurostatBySymbol:
    """Test Eurostat symbol-based queries."""

    def test_symbol_51640(self):
        """Test: te.getEurostatData(symbol='51640')"""
        result = te.getEurostatData(symbol="51640")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEurostatByCategoryGroup:
    """Test Eurostat category_group filtering."""

    def test_category_group_poverty(self):
        """Test: te.getEurostatData(category_group='Poverty')"""
        result = te.getEurostatData(category_group="Poverty")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEurostatByCategory:
    """Test Eurostat category filtering."""

    def test_category_poverty_risk(self):
        """Test: te.getEurostatData(category='People at risk of income poverty after social transfers')"""
        result = te.getEurostatData(
            category="People at risk of income poverty after social transfers"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEurostatByCountry:
    """Test Eurostat country filtering."""

    def test_country_denmark(self):
        """Test: te.getEurostatData(country='Denmark')"""
        result = te.getEurostatData(country="Denmark")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEurostatCountryWithFilters:
    """Test Eurostat country with additional filters."""

    def test_country_denmark_category_group_interest_rates(self):
        """Test: te.getEurostatData(country='Denmark', category_group='Interest rates')"""
        result = te.getEurostatData(country="Denmark", category_group="Interest rates")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_country_eu_category_unemployment(self):
        """Test: te.getEurostatData(country='European Union', category='Harmonised unemployment rate: Females')"""
        result = te.getEurostatData(
            country="European Union", category="Harmonised unemployment rate: Females"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalEurostat:
    """Test historical Eurostat data endpoints."""

    def test_historical_id_only(self):
        """Test: te.getHistoricalEurostat(ID='24804')"""
        result = te.getHistoricalEurostat(ID="24804")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)
        # Historical data should have date and value fields
        keys = [k.lower() for k in first_item.keys()]
        assert any(key in ["date", "datetime"] for key in keys)

    def test_historical_with_init_date(self):
        """Test: te.getHistoricalEurostat(ID='24804', initDate='2015-01-01')"""
        result = te.getHistoricalEurostat(ID="24804", initDate="2015-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_with_date_range(self):
        """Test: te.getHistoricalEurostat(ID='24804', initDate='2016-01-01', endDate='2020-01-01')"""
        result = te.getHistoricalEurostat(
            ID="24804", initDate="2016-01-01", endDate="2020-01-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        # Check structure
        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEurostatOutputFormats:
    """Test different output formats."""

    def test_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getEurostatData(lists="countries", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getEurostatData(lists="countries", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_output_format_raw(self):
        """Test raw output format."""
        result = te.getEurostatData(lists="countries", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

    def test_historical_output_format_df(self):
        """Test DataFrame output for historical data."""
        result = te.getHistoricalEurostat(ID="24804", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
