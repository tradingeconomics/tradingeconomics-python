"""
Integration tests for Financials, Earnings, Dividends, IPO, and Stock Splits modules.

Tests the following API calls with guest:guest credentials:

Financials:
- te.getFinancialsDataByCategory(category='assets')
- te.getFinancialsData(symbol='aapl:us')
- te.getFinancialsData()
- te.getFinancialsData(country='united states')
- te.getFinancialsData(country=['spain', 'germany'])
- te.getSectors()
- te.getFinancialsCategoryList()
- te.getFinancialsHistorical(symbol='aapl:us', category='assets')
- te.getFinancialsHistorical(symbol=['aapl:us', 'msft:us'], category='assets')
- te.getFinancialsHistorical(symbol='aapl:us', category='assets', initDate='2022-01-01', endDate='2023-01-01')

Earnings:
- te.getEarnings()
- te.getEarnings(initDate='2017-01-01')
- te.getEarnings(initDate='2017-01-01', endDate='2017-12-31')
- te.getEarnings(symbols='aapl:us', initDate='2017-01-01')
- te.getEarnings(symbols='aapl:us', initDate='2016-01-01', endDate='2017-12-31')
- te.getEarnings(country='mexico')
- te.getEarnings(country='mexico', initDate='2016-01-01', endDate='2023-12-31')
- te.getEarnings(index='ndx:ind')
- te.getEarnings(index='ndx:ind', initDate='2016-01-01', endDate='2023-12-31')
- te.getEarnings(sector='materials')
- te.getEarnings(sector='materials', initDate='2016-01-01', endDate='2023-12-31')

Dividends:
- te.getDividends(startDate='2023-01-01', endDate='2024-01-01')
- te.getDividends(symbols='aapl:us', startDate='2023-01-01', endDate='2024-01-01')

IPO:
- te.getIpo(ticker=['RRKA'])
- te.getIpo(ticker=['RRKA'], startDate='2023-09-01', endDate='2023-12-01')
- te.getIpo(country=['India'])
- te.getIpo(country=['India'], startDate='2023-09-01', endDate='2023-12-01')

Stock Splits:
- te.getStockSplits()
- te.getStockSplits(ticker='DSX')
- te.getStockSplits(country='india')
- te.getStockSplits(startDate='2025-01-01', endDate='2025-12-01')

These tests validate API endpoint availability and data structure with free access.
"""

import pytest
import tradingeconomics as te
import pandas as pd
import time


# Configure API access
te.login("guest:guest")


class TestFinancialsData:
    """Test Financials data endpoints."""

    def test_financials_by_category_assets(self):
        """Test: te.getFinancialsDataByCategory(category='assets')"""
        result = te.getFinancialsDataByCategory(category="assets")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_financials_by_symbol(self):
        """Test: te.getFinancialsData(symbol='aapl:us')"""
        result = te.getFinancialsData(symbol="aapl:us")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_financials_all_companies(self):
        """Test: te.getFinancialsData()"""
        result = te.getFinancialsData()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_financials_by_country_single(self):
        """Test: te.getFinancialsData(country='united states')"""
        result = te.getFinancialsData(country="united states")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_financials_by_country_multiple(self):
        """Test: te.getFinancialsData(country=['spain', 'germany'])"""
        result = te.getFinancialsData(country=["spain", "germany"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFinancialsMetadata:
    """Test Financials metadata endpoints."""

    def test_sectors(self):
        """Test: te.getSectors()"""
        result = te.getSectors()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_category_list(self):
        """Test: te.getFinancialsCategoryList()"""
        result = te.getFinancialsCategoryList()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestFinancialsHistorical:
    """Test Financials historical data endpoints."""

    def test_historical_single_symbol(self):
        """Test: te.getFinancialsHistorical(symbol='aapl:us', category='assets')"""
        result = te.getFinancialsHistorical(symbol="aapl:us", category="assets")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_multiple_symbols(self):
        """Test: te.getFinancialsHistorical(symbol=['aapl:us', 'msft:us'], category='assets')"""
        result = te.getFinancialsHistorical(
            symbol=["aapl:us", "msft:us"], category="assets"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_historical_with_dates(self):
        """Test: te.getFinancialsHistorical(symbol='aapl:us', category='assets', initDate='2022-01-01', endDate='2023-01-01')"""
        result = te.getFinancialsHistorical(
            symbol="aapl:us",
            category="assets",
            initDate="2022-01-01",
            endDate="2023-01-01",
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestEarnings:
    """Test Earnings endpoints."""

    def test_earnings_no_filters(self):
        """Test: te.getEarnings()"""
        result = te.getEarnings()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_with_init_date(self):
        """Test: te.getEarnings(initDate='2017-01-01')"""
        result = te.getEarnings(initDate="2017-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_with_date_range(self):
        """Test: te.getEarnings(initDate='2017-01-01', endDate='2017-12-31')"""
        result = te.getEarnings(initDate="2017-01-01", endDate="2017-12-31")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_symbol_with_date(self):
        """Test: te.getEarnings(symbols='aapl:us', initDate='2017-01-01')"""
        result = te.getEarnings(symbols="aapl:us", initDate="2017-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_symbol_with_date_range(self):
        """Test: te.getEarnings(symbols='aapl:us', initDate='2016-01-01', endDate='2017-12-31')"""
        result = te.getEarnings(
            symbols="aapl:us", initDate="2016-01-01", endDate="2017-12-31"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_country(self):
        """Test: te.getEarnings(country='mexico')"""
        result = te.getEarnings(country="mexico")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_country_with_dates(self):
        """Test: te.getEarnings(country='mexico', initDate='2016-01-01', endDate='2023-12-31')"""
        result = te.getEarnings(
            country="mexico", initDate="2016-01-01", endDate="2023-12-31"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    @pytest.mark.requires_paid_api
    def test_earnings_by_index(self):
        """Test: te.getEarnings(index='ndx:ind')

        Note: This endpoint may require paid API access.
        """
        result = te.getEarnings(index="ndx:ind")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    @pytest.mark.requires_paid_api
    def test_earnings_by_index_with_dates(self):
        """Test: te.getEarnings(index='ndx:ind', initDate='2016-01-01', endDate='2023-12-31')

        Note: This endpoint may require paid API access.
        """
        result = te.getEarnings(
            index="ndx:ind", initDate="2016-01-01", endDate="2023-12-31"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_sector(self):
        """Test: te.getEarnings(sector='materials')"""
        result = te.getEarnings(sector="materials")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_earnings_by_sector_with_dates(self):
        """Test: te.getEarnings(sector='materials', initDate='2016-01-01', endDate='2023-12-31')"""
        result = te.getEarnings(
            sector="materials", initDate="2016-01-01", endDate="2023-12-31"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestDividends:
    """Test Dividends endpoints."""

    def test_dividends_date_range(self):
        """Test: te.getDividends(startDate='2023-01-01', endDate='2024-01-01')"""
        result = te.getDividends(startDate="2023-01-01", endDate="2024-01-01")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_dividends_with_symbol(self):
        """Test: te.getDividends(symbols='aapl:us', startDate='2023-01-01', endDate='2024-01-01')"""
        result = te.getDividends(
            symbols="aapl:us", startDate="2023-01-01", endDate="2024-01-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestIPO:
    """Test IPO endpoints."""

    def test_ipo_by_ticker(self):
        """Test: te.getIpo(ticker=['RRKA'])"""
        result = te.getIpo(ticker=["RRKA"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_ipo_by_ticker_with_dates(self):
        """Test: te.getIpo(ticker=['RRKA'], startDate='2023-09-01', endDate='2023-12-01')"""
        result = te.getIpo(
            ticker=["RRKA"], startDate="2023-09-01", endDate="2023-12-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_ipo_by_country(self):
        """Test: te.getIpo(country=['India'])"""
        result = te.getIpo(country=["India"])

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_ipo_by_country_with_dates(self):
        """Test: te.getIpo(country=['India'], startDate='2023-09-01', endDate='2023-12-01')"""
        result = te.getIpo(
            country=["India"], startDate="2023-09-01", endDate="2023-12-01"
        )

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)


class TestStockSplits:
    """Test Stock Splits endpoints."""

    def test_stock_splits_all(self):
        """Test: te.getStockSplits()"""
        result = te.getStockSplits()

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stock_splits_by_ticker(self):
        """Test: te.getStockSplits(ticker='DSX')"""
        result = te.getStockSplits(ticker="DSX")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stock_splits_by_country(self):
        """Test: te.getStockSplits(country='india')"""
        result = te.getStockSplits(country="india")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0

        first_item = result[0]
        assert isinstance(first_item, dict)

    def test_stock_splits_with_dates(self):
        """Test: te.getStockSplits(startDate='2025-01-01', endDate='2025-12-01')"""
        result = te.getStockSplits(startDate="2025-01-01", endDate="2025-12-01")

        assert result is not None
        assert isinstance(result, list)
        # Note: May have 0 results if no splits in this period
        assert isinstance(result, list)


class TestOutputFormats:
    """Test different output formats."""

    def test_financials_output_format_dict(self):
        """Test dict output format (default)."""
        result = te.getFinancialsData(symbol="aapl:us", output_type="dict")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        assert isinstance(result[0], dict)

    def test_financials_output_format_df(self):
        """Test DataFrame output format."""
        result = te.getFinancialsData(symbol="aapl:us", output_type="df")

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_financials_output_format_raw(self):
        """Test raw output format."""
        result = te.getFinancialsData(symbol="aapl:us", output_type="raw")

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
