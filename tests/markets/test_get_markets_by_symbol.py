import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsBySymbol
from tradingeconomics import glob


class TestGetMarketsBySymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"symbol": "indu"})
    def test_get_markets_by_symbol_single(self, mock_request):
        # Get markets data for single symbol
        result = getMarketsBySymbol(symbols="indu:ind")

        expected_url = (
            "https://api.tradingeconomics.com/markets/symbol/indu%3Aind?c=TESTKEY"
        )

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"symbol": "indu"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"symbol": "multiple"}
    )
    def test_get_markets_by_symbol_multiple(self, mock_request):
        # Get markets data for multiple symbols
        result = getMarketsBySymbol(symbols=["aapl:us", "indu:ind"])

        expected_url = "https://api.tradingeconomics.com/markets/symbol/aapl%3Aus%2Cindu%3Aind?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"symbol": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"symbol": "raw"})
    def test_get_markets_by_symbol_with_output_type(self, mock_request):
        # Get markets data with output type
        result = getMarketsBySymbol(symbols="indu:ind", output_type="raw")

        expected_url = (
            "https://api.tradingeconomics.com/markets/symbol/indu%3Aind?c=TESTKEY"
        )

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"symbol": "raw"})
