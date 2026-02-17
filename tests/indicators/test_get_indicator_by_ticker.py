import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getIndicatorByTicker
from tradingeconomics import glob


class TestGetIndicatorByTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"ticker": "ok"})
    def test_get_indicator_by_ticker(self, mock_request):
        # Get indicator by ticker
        result = getIndicatorByTicker(ticker="USURTOT")

        expected_url = "/country/ticker/USURTOT"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"ticker": "multiple"},
    )
    def test_get_indicator_by_multiple_tickers(self, mock_request):
        # Get indicators by multiple tickers
        result = getIndicatorByTicker(ticker=["WGDPCHIN", "USURTOT"])

        expected_url = "/country/ticker/WGDPCHIN,USURTOT"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.indicators.fn.dataRequest", return_value={"ticker": "df"})
    def test_get_indicator_by_ticker_with_output_type(self, mock_request):
        # Get indicator with output type
        result = getIndicatorByTicker(ticker="USURTOT", output_type="df")

        expected_url = "/country/ticker/USURTOT"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ticker": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "ticker": "data"},
    )
    def test_get_indicator_by_ticker_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getIndicatorByTicker(ticker="USURTOT", output_type="raw")

        expected_url = "/country/ticker/USURTOT"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "ticker": "data"})

    def test_get_indicator_by_ticker_missing_parameter(self):
        # Test error when ticker is missing
        result = getIndicatorByTicker()

        self.assertEqual(result, "Ticker is required")
