"""
Integration tests for Indicators and Historical modules.

Tests the following API calls with guest:guest credentials:

Indicators:
- te.getIndicatorData(country='mexico')
- te.getIndicatorData(country=['mexico', 'sweden'])
- te.getIndicatorByCategoryGroup(country='mexico', category_group='gdp')
- te.getIndicatorData(indicators='gdp')
- te.getIndicatorByTicker(ticker='usurtot')
- te.getIndicatorData()
- te.getAllCountries()
- te.getPeers(ticker='CPI YOY')
- te.getPeers(country='mexico', category='inflation rate')
- te.getDiscontinuedIndicator()
- te.getDiscontinuedIndicator(country='united states')
- te.getDiscontinuedIndicator(country=['united states', 'china'])

Historical:
- te.getHistoricalData(country='mexico', indicator='gdp')
- te.getHistoricalData(country=['mexico', 'sweden'], indicator=['gdp','population'], initDate='2015-01-01')
- te.getHistoricalData(country=['mexico', 'sweden'], indicator=['gdp','population'], initDate='2015-01-01', endDate='2015-12-31')
- te.getHistoricalByTicker(ticker='USURTOT', start_date='2015-03-01')
- te.getHistoricalLatest(country=['United States', 'Brazil'], date='2025-08-26')
- te.getHistoricalUpdates()

Latest Updates:
- te.getLatestUpdates()
- te.getLatestUpdates(init_date='2018-01-01')
- te.getLatestUpdates(init_date='2021-10-18', time='15:20')
- te.getLatestUpdates(country='portugal')
- te.getLatestUpdates(country=['portugal', 'spain'])
- te.getLatestUpdates(country='portugal', init_date='2018-01-01')

Indicator Changes:
- te.getIndicatorChanges()
- te.getIndicatorChanges(start_date='2024-10-01')

Credit Ratings:
- te.getCreditRatings()
- te.getCreditRatingsUpdates()
- te.getCreditRatings(country='sweden')
- te.getCreditRatings(country=['mexico','sweden'])
- te.getHistoricalCreditRatings(initDate='2022-01-01', endDate='2023-01-01')
- te.getHistoricalCreditRatings(country='sweden', initDate='2000-01-01', endDate='2023-01-01')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time


# Configure API access
te.login("guest:guest")


class TestIndicatorData:
    """Test Indicator data endpoints."""

    def test_indicator_by_country_single(self):
        """Test: te.getIndicatorData(country='mexico')"""
        result = te.getIndicatorData(country="mexico")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_indicator_by_country_multiple(self):
        """Test: te.getIndicatorData(country=['mexico', 'sweden'])"""
        result = te.getIndicatorData(country=["mexico", "sweden"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_indicator_by_name(self):
        """Test: te.getIndicatorData(indicators='gdp')"""
        result = te.getIndicatorData(indicators="gdp")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_indicator_all(self):
        """Test: te.getIndicatorData()"""
        result = te.getIndicatorData()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestIndicatorByCategoryGroup:
    """Test Indicator by category group."""

    def test_indicator_by_category_group(self):
        """Test: te.getIndicatorByCategoryGroup(country='mexico', category_group='gdp')"""
        result = te.getIndicatorByCategoryGroup(country="mexico", category_group="gdp")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestIndicatorByTicker:
    """Test Indicator by ticker."""

    def test_indicator_by_ticker(self):
        """Test: te.getIndicatorByTicker(ticker='usurtot')"""
        result = te.getIndicatorByTicker(ticker="usurtot")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestIndicatorMetadata:
    """Test Indicator metadata endpoints."""

    def test_all_countries(self):
        """Test: te.getAllCountries()"""
        result = te.getAllCountries()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestPeers:
    """Test Peers endpoints."""

    def test_peers_by_ticker(self):
        """Test: te.getPeers(ticker='CPI YOY')"""
        result = te.getPeers(ticker="CPI YOY")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_peers_by_country_category(self):
        """Test: te.getPeers(country='mexico', category='inflation rate')"""
        result = te.getPeers(country="mexico", category="inflation rate")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestDiscontinuedIndicator:
    """Test Discontinued indicator endpoints."""

    def test_discontinued_all(self):
        """Test: te.getDiscontinuedIndicator()"""
        result = te.getDiscontinuedIndicator()

        assert result is not None
        assert isinstance(result, list)
        # May be empty if no discontinued indicators
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)

    def test_discontinued_by_country_single(self):
        """Test: te.getDiscontinuedIndicator(country='united states')"""
        result = te.getDiscontinuedIndicator(country="united states")

        assert result is not None
        assert isinstance(result, list)
        # May be empty if no discontinued indicators for this country
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)

    def test_discontinued_by_country_multiple(self):
        """Test: te.getDiscontinuedIndicator(country=['united states', 'china'])"""
        result = te.getDiscontinuedIndicator(country=["united states", "china"])

        assert result is not None
        assert isinstance(result, list)
        # May be empty if no discontinued indicators for these countries
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)


class TestHistoricalData:
    """Test Historical data endpoints."""

    def test_historical_country_indicator(self):
        """Test: te.getHistoricalData(country='mexico', indicator='gdp')"""
        result = te.getHistoricalData(country="mexico", indicator="gdp")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_multiple_with_init_date(self):
        """Test: te.getHistoricalData(country=['mexico', 'sweden'], indicator=['gdp','population'], initDate='2015-01-01')"""
        result = te.getHistoricalData(
            country=["mexico", "sweden"],
            indicator=["gdp", "population"],
            initDate="2015-01-01",
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_multiple_with_date_range(self):
        """Test: te.getHistoricalData(country=['mexico', 'sweden'], indicator=['gdp','population'], initDate='2015-01-01', endDate='2015-12-31')"""
        result = te.getHistoricalData(
            country=["mexico", "sweden"],
            indicator=["gdp", "population"],
            initDate="2015-01-01",
            endDate="2015-12-31",
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalByTicker:
    """Test Historical by ticker endpoints."""

    def test_historical_by_ticker(self):
        """Test: te.getHistoricalByTicker(ticker='USURTOT', start_date='2015-03-01')"""
        result = te.getHistoricalByTicker(ticker="USURTOT", start_date="2015-03-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalLatest:
    """Test Historical Latest endpoints."""

    def test_historical_latest_multiple_countries_with_date(self):
        """Test: te.getHistoricalLatest(country=['United States', 'Brazil'], date='2024-08-26')"""
        result = te.getHistoricalLatest(
            country=["United States", "Brazil"], date="2024-08-26"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalUpdates:
    """Test Historical updates endpoints."""

    def test_historical_updates(self):
        """Test: te.getHistoricalUpdates()"""
        result = te.getHistoricalUpdates()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestLatestUpdates:
    """Test Latest updates endpoints."""

    def test_latest_updates_no_filters(self):
        """Test: te.getLatestUpdates()"""
        result = te.getLatestUpdates()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_latest_updates_with_date(self):
        """Test: te.getLatestUpdates(init_date='2018-01-01')"""
        result = te.getLatestUpdates(init_date="2018-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_latest_updates_with_datetime(self):
        """Test: te.getLatestUpdates(init_date='2021-10-18', time='15:20')"""
        result = te.getLatestUpdates(init_date="2021-10-18", time="15:20")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_latest_updates_by_country_single(self):
        """Test: te.getLatestUpdates(country='portugal')"""
        result = te.getLatestUpdates(country="portugal")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_latest_updates_by_country_multiple(self):
        """Test: te.getLatestUpdates(country=['portugal', 'spain'])"""
        result = te.getLatestUpdates(country=["portugal", "spain"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_latest_updates_country_with_date(self):
        """Test: te.getLatestUpdates(country='portugal', init_date='2018-01-01')"""
        result = te.getLatestUpdates(country="portugal", init_date="2018-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestIndicatorChanges:
    """Test Indicator changes endpoints."""

    def test_indicator_changes_no_filters(self):
        """Test: te.getIndicatorChanges()"""
        result = te.getIndicatorChanges()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_indicator_changes_with_date(self):
        """Test: te.getIndicatorChanges(start_date='2024-10-01')"""
        result = te.getIndicatorChanges(start_date="2024-10-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestCreditRatings:
    """Test Credit ratings endpoints."""

    def test_credit_ratings_all(self):
        """Test: te.getCreditRatings()"""
        result = te.getCreditRatings()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_credit_ratings_updates(self):
        """Test: te.getCreditRatingsUpdates()"""
        result = te.getCreditRatingsUpdates()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_credit_ratings_by_country_single(self):
        """Test: te.getCreditRatings(country='sweden')"""
        result = te.getCreditRatings(country="sweden")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_credit_ratings_by_country_multiple(self):
        """Test: te.getCreditRatings(country=['mexico','sweden'])"""
        result = te.getCreditRatings(country=["mexico", "sweden"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalCreditRatings:
    """Test Historical credit ratings endpoints."""

    def test_historical_credit_ratings_dates_only(self):
        """Test: te.getHistoricalCreditRatings(initDate='2022-01-01', endDate='2023-01-01')"""
        result = te.getHistoricalCreditRatings(
            initDate="2022-01-01", endDate="2023-01-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_credit_ratings_with_country(self):
        """Test: te.getHistoricalCreditRatings(country='sweden', initDate='2000-01-01', endDate='2023-01-01')"""
        result = te.getHistoricalCreditRatings(
            country="sweden", initDate="2000-01-01", endDate="2023-01-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestOutputFormats:
    """Test different output formats."""

    def test_indicator_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getIndicatorData(country="mexico", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_indicator_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getIndicatorData(country="mexico", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_indicator_output_format_raw(self):
        """Test raw output format."""
        result = te.getIndicatorData(country="mexico", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
