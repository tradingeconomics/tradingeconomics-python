"""
Integration tests for Markets module.

Tests the following API calls with guest:guest credentials:

Markets Data:
- te.getMarketsData(marketsField='commodities')
- te.getMarketsData(marketsField='currency')
- te.getCurrencyCross(cross='EUR')
- te.getMarketsData(marketsField='crypto')
- te.getMarketsData(marketsField='index')
- te.getMarketsData(marketsField='bond', type='10Y')

Markets by Symbol:
- te.getMarketsBySymbol(symbols='aapl:us')
- te.getMarketsBySymbol(symbols=['aapl:us', 'gac:com'])

Markets Peers:
- te.getMarketsPeers(symbols='aapl:us')

Markets Components:
- te.getMarketsComponents(symbols='psi20:ind')
- te.getMarketsComponents(symbols=['indu:ind', 'psi20:ind'])

Stocks by Country:
- te.getStocksByCountry(country='united states')
- te.getStocksByCountry(country=['united states', 'nigeria'])

Markets by Country:
- te.getMarketsByCountry(country='united states')

Markets Forecasts:
- te.getMarketsForecasts(category='index')
- te.getMarketsForecasts(symbol='aapl:us')
- te.getMarketsForecasts(symbol=['AAPL:US','DAX:IND','INDU:IND'])

Stock Descriptions:
- te.getMarketsStockDescriptions(symbol='aapl:us')
- te.getMarketsStockDescriptions(symbol=['aapl:us', 'fb:us'])
- te.getMarketsStockDescriptions(country='france')

Markets Symbology:
- te.getMarketsSymbology(symbol='aapl:us')
- te.getMarketsSymbology(country='mexico')
- te.getMarketsSymbology(ticker='aapl')
- te.getMarketsSymbology(isin='US0378331005')

Historical Markets:
- te.getHistorical(symbol='aapl:us')
- te.getHistorical(symbol=['aapl:us','gac:com'])
- te.fetchMarkets(symbol=['aapl:us','gac:com'], initDate='2017-08-01')
- te.fetchMarkets(symbol=['aapl:us','gac:com'], initDate='2017-08-01', endDate='2017-08-08')

Markets Search:
- te.getMarketsSearch(country='united states')
- te.getMarketsSearch(country='united states', category='index')
- te.getMarketsSearch(country='united states', category=['index', 'markets'])
- te.getMarketsSearch(country='msft')

Markets Intraday:
- te.getMarketsIntraday(symbols=['aapl:us','stx:us'])
- te.getMarketsIntraday(symbols='aapl:us', initDate='2017-08-10 15:30')
- te.getMarketsIntraday(symbols='aapl:us', initDate='2017-08-01', endDate='2017-08-08')

Markets Intraday by Interval:
- te.getMarketsIntradayByInterval(symbol='aapl:us', initDate='2020-01-01', endDate='2020-12-01', interval='10m')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd


# Configure API access
te.login("guest:guest")


class TestMarketsData:
    """Test Markets data endpoints."""

    def test_markets_data_commodities(self):
        """Test: te.getMarketsData(marketsField='commodities')"""
        result = te.getMarketsData(marketsField="commodities")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_data_currency(self):
        """Test: te.getMarketsData(marketsField='currency')"""
        result = te.getMarketsData(marketsField="currency")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_data_crypto(self):
        """Test: te.getMarketsData(marketsField='crypto')"""
        result = te.getMarketsData(marketsField="crypto")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_data_index(self):
        """Test: te.getMarketsData(marketsField='index')"""
        result = te.getMarketsData(marketsField="index")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_data_bond(self):
        """Test: te.getMarketsData(marketsField='bond', type='10Y')"""
        result = te.getMarketsData(marketsField="bond", type="10Y")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestCurrencyCross:
    """Test Currency cross endpoints."""

    def test_currency_cross(self):
        """Test: te.getCurrencyCross(cross='EUR')"""
        result = te.getCurrencyCross(cross="EUR")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsBySymbol:
    """Test Markets by symbol endpoints."""

    def test_markets_by_symbol_single(self):
        """Test: te.getMarketsBySymbol(symbols='aapl:us')"""
        result = te.getMarketsBySymbol(symbols="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_by_symbol_multiple(self):
        """Test: te.getMarketsBySymbol(symbols=['aapl:us', 'gac:com'])"""
        result = te.getMarketsBySymbol(symbols=["aapl:us", "gac:com"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsPeers:
    """Test Markets peers endpoints."""

    def test_markets_peers(self):
        """Test: te.getMarketsPeers(symbols='aapl:us')"""
        result = te.getMarketsPeers(symbols="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsComponents:
    """Test Markets components endpoints."""

    def test_markets_components_single(self):
        """Test: te.getMarketsComponents(symbols='psi20:ind')"""
        result = te.getMarketsComponents(symbols="psi20:ind")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_components_multiple(self):
        """Test: te.getMarketsComponents(symbols=['indu:ind', 'psi20:ind'])"""
        result = te.getMarketsComponents(symbols=["indu:ind", "psi20:ind"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestStocksByCountry:
    """Test Stocks by country endpoints."""

    def test_stocks_by_country_single(self):
        """Test: te.getStocksByCountry(country='united states')"""
        result = te.getStocksByCountry(country="united states")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stocks_by_country_multiple(self):
        """Test: te.getStocksByCountry(country=['united states', 'nigeria'])"""
        result = te.getStocksByCountry(country=["united states", "nigeria"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsByCountry:
    """Test Markets by country endpoints."""

    def test_markets_by_country(self):
        """Test: te.getMarketsByCountry(country='united states')"""
        result = te.getMarketsByCountry(country="united states")

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


class TestMarketsStockDescriptions:
    """Test Markets stock descriptions endpoints."""

    def test_stock_descriptions_by_symbol_single(self):
        """Test: te.getMarketsStockDescriptions(symbol='aapl:us')"""
        result = te.getMarketsStockDescriptions(symbol="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stock_descriptions_by_symbol_multiple(self):
        """Test: te.getMarketsStockDescriptions(symbol=['aapl:us', 'fb:us'])"""
        result = te.getMarketsStockDescriptions(symbol=["aapl:us", "fb:us"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stock_descriptions_by_country(self):
        """Test: te.getMarketsStockDescriptions(country='france')"""
        result = te.getMarketsStockDescriptions(country="france")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsSymbology:
    """Test Markets symbology endpoints."""

    def test_markets_symbology_by_symbol(self):
        """Test: te.getMarketsSymbology(symbol='aapl:us')"""
        result = te.getMarketsSymbology(symbol="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_symbology_by_country(self):
        """Test: te.getMarketsSymbology(country='mexico')"""
        result = te.getMarketsSymbology(country="mexico")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_symbology_by_ticker(self):
        """Test: te.getMarketsSymbology(ticker='aapl')"""
        result = te.getMarketsSymbology(ticker="aapl")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_symbology_by_isin(self):
        """Test: te.getMarketsSymbology(isin='US0378331005')"""
        result = te.getMarketsSymbology(isin="US0378331005")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestHistoricalMarkets:
    """Test Historical markets endpoints."""

    def test_get_historical_single_symbol(self):
        """Test: te.getHistorical(symbol='aapl:us')"""
        result = te.getHistorical(symbol="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_get_historical_multiple_symbols(self):
        """Test: te.getHistorical(symbol=['aapl:us','gac:com'])"""
        result = te.getHistorical(symbol=["aapl:us", "gac:com"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_fetch_markets_with_init_date(self):
        """Test: te.fetchMarkets(symbol=['aapl:us','gac:com'], initDate='2017-08-01')"""
        result = te.fetchMarkets(symbol=["aapl:us", "gac:com"], initDate="2017-08-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_fetch_markets_with_date_range(self):
        """Test: te.fetchMarkets(symbol=['aapl:us','gac:com'], initDate='2017-08-01', endDate='2017-08-08')"""
        result = te.fetchMarkets(
            symbol=["aapl:us", "gac:com"], initDate="2017-08-01", endDate="2017-08-08"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestMarketsSearch:
    """Test Markets search endpoints."""

    def test_markets_search_by_country(self):
        """Test: te.getMarketsSearch(country='united states')"""
        result = te.getMarketsSearch(country="united states")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_search_by_country_and_category_single(self):
        """Test: te.getMarketsSearch(country='united states', category='index')"""
        result = te.getMarketsSearch(country="united states", category="index")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_search_by_country_and_category_multiple(self):
        """Test: te.getMarketsSearch(country='united states', category=['index', 'markets'])"""
        result = te.getMarketsSearch(
            country="united states", category=["index", "markets"]
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_markets_search_by_ticker_name(self):
        """Test: te.getMarketsSearch(country='msft')"""
        result = te.getMarketsSearch(country="msft")

        assert result is not None
        assert isinstance(result, list)
        # May be empty if searching by ticker in 'country' parameter
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)


class TestMarketsIntraday:
    """Test Markets intraday endpoints."""

    def test_markets_intraday_multiple_symbols(self):
        """Test: te.getMarketsIntraday(symbols=['aapl:us','stx:us'])"""
        result = te.getMarketsIntraday(symbols=["aapl:us", "stx:us"])

        assert result is not None
        assert isinstance(result, list)
        # May be empty with guest credentials
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)

    def test_markets_intraday_with_init_datetime(self):
        """Test: te.getMarketsIntraday(symbols='aapl:us', initDate='2017-08-10 15:30')"""
        result = te.getMarketsIntraday(symbols="aapl:us", initDate="2017-08-10 15:30")

        assert result is not None
        assert isinstance(result, list)
        # May be empty with guest credentials
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)

    def test_markets_intraday_with_date_range(self):
        """Test: te.getMarketsIntraday(symbols='aapl:us', initDate='2017-08-01', endDate='2017-08-08')"""
        result = te.getMarketsIntraday(
            symbols="aapl:us", initDate="2017-08-01", endDate="2017-08-08"
        )

        assert result is not None
        assert isinstance(result, list)
        # May be empty with guest credentials
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)


class TestMarketsIntradayByInterval:
    """Test Markets intraday by interval endpoints."""

    def test_markets_intraday_by_interval(self):
        """Test: te.getMarketsIntradayByInterval(symbol='aapl:us', initDate='2020-01-01', endDate='2020-12-01', interval='10m')"""
        result = te.getMarketsIntradayByInterval(
            symbol="aapl:us",
            initDate="2020-01-01",
            endDate="2020-12-01",
            interval="10m",
        )

        assert result is not None
        assert isinstance(result, list)
        # May be empty with guest credentials
        if len(result) > 0:
            first_item = result[0]
            assert isinstance(first_item, dict)


class TestOutputFormats:
    """Test different output formats."""

    def test_markets_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getMarketsData(marketsField="commodities", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_markets_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getMarketsData(marketsField="commodities", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_markets_output_format_raw(self):
        """Test raw output format."""
        result = te.getMarketsData(marketsField="commodities", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
