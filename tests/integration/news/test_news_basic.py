"""
Integration tests for News module.

Tests the following API calls with guest:guest credentials:

News:
- te.getNews()
- te.getNews(start=150, limit=5)
- te.getNews(start_date='2021-02-02', end_date='2021-03-03')
- te.getNews(country='mexico')
- te.getNews(country='mexico', start_date='2021-02-02', end_date='2021-03-03')
- te.getNews(indicator='inflation rate')
- te.getNews(indicator=['inflation rate','gdp'])
- te.getNews(indicator='inflation rate', start_date='2021-02-02', end_date='2021-03-03')
- te.getNews(indicator=['inflation rate', 'imports'], start_date='2021-02-02', end_date='2021-03-03')
- te.getNews(country='mexico', indicator='inflation rate')
- te.getNews(country='mexico', indicator='inflation rate', start_date='2021-02-02', end_date='2021-03-03')
- te.getNews(type='markets')
- te.getNews(ticker='CZCAEUR')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time


# Configure API access
te.login("guest:guest")


class TestNewsBasic:
    """Test basic news endpoints."""

    def test_news_all(self):
        """Test: te.getNews()"""
        result = te.getNews()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_with_start_limit(self):
        """Test: te.getNews(start=150, limit=5)"""
        result = te.getNews(start=150, limit=5)

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert len(result) <= 5  # Should respect limit

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_with_date_range(self):
        """Test: te.getNews(start_date='2021-02-02', end_date='2021-03-03')"""
        result = te.getNews(start_date="2021-02-02", end_date="2021-03-03")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsByCountry:
    """Test news by country filtering."""

    def test_news_by_country(self):
        """Test: te.getNews(country='mexico')"""
        result = te.getNews(country="mexico")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_by_country_with_dates(self):
        """Test: te.getNews(country='mexico', start_date='2021-02-02', end_date='2021-03-03')"""
        result = te.getNews(
            country="mexico", start_date="2021-02-02", end_date="2021-03-03"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsByIndicator:
    """Test news by indicator filtering."""

    def test_news_by_indicator_single(self):
        """Test: te.getNews(indicator='inflation rate')"""
        result = te.getNews(indicator="inflation rate")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_by_indicator_multiple(self):
        """Test: te.getNews(indicator=['inflation rate','gdp'])"""
        result = te.getNews(indicator=["inflation rate", "gdp"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_by_indicator_with_dates(self):
        """Test: te.getNews(indicator='inflation rate', start_date='2021-02-02', end_date='2021-03-03')"""
        result = te.getNews(
            indicator="inflation rate", start_date="2021-02-02", end_date="2021-03-03"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_by_indicator_multiple_with_dates(self):
        """Test: te.getNews(indicator=['inflation rate', 'imports'], start_date='2021-02-02', end_date='2021-03-03')"""
        result = te.getNews(
            indicator=["inflation rate", "imports"],
            start_date="2021-02-02",
            end_date="2021-03-03",
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsByCountryAndIndicator:
    """Test news by country and indicator combined."""

    def test_news_by_country_and_indicator(self):
        """Test: te.getNews(country='mexico', indicator='inflation rate')"""
        result = te.getNews(country="mexico", indicator="inflation rate")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_news_by_country_and_indicator_with_dates(self):
        """Test: te.getNews(country='mexico', indicator='inflation rate', start_date='2021-02-02', end_date='2021-03-03')"""
        result = te.getNews(
            country="mexico",
            indicator="inflation rate",
            start_date="2021-02-02",
            end_date="2021-03-03",
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsByType:
    """Test news by type filtering."""

    def test_news_by_type_markets(self):
        """Test: te.getNews(type='markets')"""
        result = te.getNews(type="markets")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsByTicker:
    """Test news by ticker filtering."""

    def test_news_by_ticker(self):
        """Test: te.getNews(ticker='CZCAEUR')"""
        result = te.getNews(ticker="CZCAEUR")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestNewsOutputFormats:
    """Test different output formats."""

    def test_news_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getNews(country="mexico", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_news_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getNews(country="mexico", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_news_output_format_raw(self):
        """Test raw output format."""
        result = te.getNews(country="mexico", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
