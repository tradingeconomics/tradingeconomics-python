import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalByTicker
from tradingeconomics import glob


class TestGetHistoricalByTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"ticker": "ok"})
    def test_historical_by_ticker_no_dates(self, mock_request, mock_string_or_list):
        # Get historical data by ticker without dates
        result = getHistoricalByTicker(ticker="USURTOT")

        expected_url = "/historical/ticker/USURTOT/None"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"ticker": "with_start"},
    )
    def test_historical_by_ticker_with_start_date(
        self, mock_request, mock_string_or_list, mock_validate
    ):
        # Get historical data by ticker with start date
        result = getHistoricalByTicker(ticker="USURTOT", start_date="2015-03-01")

        expected_url = "/historical/ticker/USURTOT/2015-03-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "with_start"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"ticker": "with_dates"},
    )
    def test_historical_by_ticker_with_date_range(
        self, mock_request, mock_string_or_list, mock_validate
    ):
        # Get historical data by ticker with date range
        result = getHistoricalByTicker(
            ticker="USURTOT", start_date="2015-03-01", end_date="2015-09-30"
        )

        expected_url = "/historical/ticker/USURTOT/2015-03-01/2015-09-30"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value=[{"value": 100}])
    def test_historical_by_ticker_with_output_type(
        self, mock_request, mock_string_or_list
    ):
        # Test with output_type parameter
        result = getHistoricalByTicker(ticker="USURTOT", output_type="df")

        expected_url = "/historical/ticker/USURTOT/None"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"raw": "json", "ticker": "USURTOT"},
    )
    def test_historical_by_ticker_output_type_raw(
        self, mock_request, mock_string_or_list
    ):
        # Test with output_type='raw' parameter
        result = getHistoricalByTicker(ticker="USURTOT", output_type="raw")

        expected_url = "/historical/ticker/USURTOT/None"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "ticker": "USURTOT"})
