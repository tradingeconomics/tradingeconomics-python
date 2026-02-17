"""
Integration tests for Forecasts module.

Tests the following API calls with guest:guest credentials:

Forecasts:
- te.getForecastData(country='mexico')
- te.getForecastData(country=['mexico', 'sweden'])
- te.getForecastData(indicator='gdp')
- te.getForecastData(indicator=['gdp', 'population'])
- te.getForecastData(country=['mexico','sweden'], indicator=['gdp','population'])
- te.getForecastByTicker(ticker='usurtot')
- te.getForecastByTicker(ticker=['usurtot', 'wgdpchin'])
- te.getForecastUpdates()
- te.getForecastUpdates(init_date='2024-10-30')
- te.getForecastUpdates(country='albania')

Markets Forecasts:
- te.getMarketsForecasts(category='index')
- te.getMarketsForecasts(symbol='aapl:us')
- te.getMarketsForecasts(symbol=['AAPL:US','DAX:IND','INDU:IND'])

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time


# Configure API access
te.login("guest:guest")


class TestForecastData:
    """Test Forecast data endpoints."""

    def test_forecast_by_country_single(self):
        """Test: te.getForecastData(country='mexico')"""
        result = te.getForecastData(country="mexico")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_by_country_multiple(self):
        """Test: te.getForecastData(country=['mexico', 'sweden'])"""
        result = te.getForecastData(country=["mexico", "sweden"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_by_indicator_single(self):
        """Test: te.getForecastData(indicator='gdp')"""
        result = te.getForecastData(indicator="gdp")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_by_indicator_multiple(self):
        """Test: te.getForecastData(indicator=['gdp', 'population'])"""
        result = te.getForecastData(indicator=["gdp", "population"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_by_country_and_indicator(self):
        """Test: te.getForecastData(country=['mexico','sweden'], indicator=['gdp','population'])"""
        result = te.getForecastData(
            country=["mexico", "sweden"], indicator=["gdp", "population"]
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestForecastByTicker:
    """Test Forecast by ticker endpoints."""

    def test_forecast_by_ticker_single(self):
        """Test: te.getForecastByTicker(ticker='usurtot')"""
        result = te.getForecastByTicker(ticker="usurtot")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_by_ticker_multiple(self):
        """Test: te.getForecastByTicker(ticker=['usurtot', 'wgdpchin'])"""
        result = te.getForecastByTicker(ticker=["usurtot", "wgdpchin"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestForecastUpdates:
    """Test Forecast updates endpoints."""

    def test_forecast_updates_no_filters(self):
        """Test: te.getForecastUpdates()"""
        result = te.getForecastUpdates()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_updates_with_init_date(self):
        """Test: te.getForecastUpdates(init_date='2024-10-30')"""
        result = te.getForecastUpdates(init_date="2024-10-30")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_forecast_updates_with_country(self):
        """Test: te.getForecastUpdates(country='albania')"""
        result = te.getForecastUpdates(country="albania")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsForecasts:
    """Test Markets forecasts endpoints."""

    def test_markets_forecasts_by_category(self):
        """Test: te.getMarketsForecasts(category='index')"""
        result = te.getMarketsForecasts(category="index")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_forecasts_by_symbol_single(self):
        """Test: te.getMarketsForecasts(symbol='aapl:us')"""
        result = te.getMarketsForecasts(symbol="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_forecasts_by_symbol_multiple(self):
        """Test: te.getMarketsForecasts(symbol=['AAPL:US','DAX:IND','INDU:IND'])"""
        result = te.getMarketsForecasts(symbol=["AAPL:US", "DAX:IND", "INDU:IND"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestForecastOutputFormats:
    """Test different output formats."""

    def test_forecast_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getForecastData(country="mexico", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_forecast_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getForecastData(country="mexico", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_forecast_output_format_raw(self):
        """Test raw output format."""
        result = te.getForecastData(country="mexico", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
