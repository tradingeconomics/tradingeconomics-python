import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalMarkets(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value={"markets": "ok"}
    )
    def test_historical_markets_symbol(self, mock_request):
        # Get historical data for markets symbol (contains colon)
        result = getHistorical(symbol="aapl:us")

        expected_url = (
            "https://api.tradingeconomics.com/markets/historical/aapl%3Aus?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"markets": "multiple"},
    )
    def test_historical_markets_multiple_symbols(self, mock_request):
        # Get historical data for multiple markets symbols
        result = getHistorical(symbol=["aapl:us", "indu:ind"])

        expected_url = "https://api.tradingeconomics.com/markets/historical/aapl%3Aus%2Cindu%3Aind?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"markets": "with_date"},
    )
    def test_historical_markets_with_init_date(self, mock_request, mock_validate):
        # Get historical data with init date
        result = getHistorical(symbol="indu:ind", initDate="2015-01-01")

        expected_url = "https://api.tradingeconomics.com/markets/historical/indu%3Aind?d1=2015-01-01&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "with_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalDB.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"markets": "with_dates"},
    )
    def test_historical_markets_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical data with date range
        result = getHistorical(
            symbol="indu:ind", initDate="2015-01-01", endDate="2017-01-01"
        )

        expected_url = "https://api.tradingeconomics.com/markets/historical/indu%3Aind?d1=2015-01-01&d2=2017-01-01&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "with_dates"})
