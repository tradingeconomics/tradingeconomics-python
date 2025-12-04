import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastByTicker
from tradingeconomics import glob


class TestGetForecastByTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.stringOrList", return_value="USURTOT")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"ticker": "ok"})
    def test_forecast_ticker_single(self, mock_request, mock_string_or_list):
        # Get forecast data for single ticker
        result = getForecastByTicker(ticker="USURTOT")

        expected_url = (
            "https://api.tradingeconomics.com/forecast/ticker/USURTOT?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.stringOrList", return_value="WGDPCHIN%2CUSURTOT"
    )
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest", return_value={"ticker": "multiple"}
    )
    def test_forecast_ticker_multiple(self, mock_request, mock_string_or_list):
        # Get forecast data for multiple tickers
        result = getForecastByTicker(ticker=["WGDPCHIN", "USURTOT"])

        expected_url = "https://api.tradingeconomics.com/forecast/ticker/WGDPCHIN%2CUSURTOT?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.stringOrList", return_value="USURTOT")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value=[{"ticker": "USURTOT"}],
    )
    def test_forecast_ticker_with_output_type(self, mock_request, mock_string_or_list):
        # Test with output_type parameter
        result = getForecastByTicker(ticker="USURTOT", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/forecast/ticker/USURTOT?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"ticker": "USURTOT"}])
