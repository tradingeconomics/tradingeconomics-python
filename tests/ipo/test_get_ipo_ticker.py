import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "ticker"})
    def test_get_ipo_by_ticker(self, mock_request):
        # Get IPO data for specific ticker
        result = getIpo(ticker="SWIN")

        expected_url = "/ipo/ticker/SWIN"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "ticker"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "tickers"})
    def test_get_ipo_by_multiple_tickers(self, mock_request):
        # Get IPO data for multiple tickers
        result = getIpo(ticker=["SWIN", "AAPL"])

        expected_url = "/ipo/ticker/SWIN,AAPL"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "tickers"})
