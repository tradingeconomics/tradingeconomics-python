import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestSymbols(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"symbol": "ok"})
    def test_symbols_parameter(self, mock_request, mock_dates):
        # Provide a symbol and ensure URL is built correctly
        result = getEarnings(symbols="msft:us")

        expected_url = "/earnings-revenues/symbol/msft:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"symbol": "ok"})
    def test_symbols_output_type_df(self, mock_request, mock_dates):
        result = getEarnings(symbols="aapl:us", output_type="df")

        expected_url = "/earnings-revenues/symbol/aapl:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"symbol": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"symbol": "ok"})
    def test_multiple_symbols(self, mock_request, mock_dates):
        result = getEarnings(symbols=["msft:us", "aapl:us", "googl:us"])

        expected_url = "/earnings-revenues/symbol/msft:us,aapl:us,googl:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "ok"})
