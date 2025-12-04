import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsPeers
from tradingeconomics import glob


class TestGetMarketsPeers(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"peers": "ok"})
    def test_get_markets_peers_single(self, mock_request):
        # Get peers for single symbol
        result = getMarketsPeers(symbols="indu:ind")

        expected_url = (
            "https://api.tradingeconomics.com/markets/peers/indu%3Aind?c=TESTKEY"
        )

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"peers": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"peers": "multiple"}
    )
    def test_get_markets_peers_multiple(self, mock_request):
        # Get peers for multiple symbols
        result = getMarketsPeers(symbols=["aapl:us", "indu:ind"])

        expected_url = "https://api.tradingeconomics.com/markets/peers/aapl%3Aus%2Cindu%3Aind?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"peers": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"peers": "raw"})
    def test_get_markets_peers_with_output_type(self, mock_request):
        # Get peers with output type
        result = getMarketsPeers(symbols=["aapl:us", "indu:ind"], output_type="raw")

        expected_url = "https://api.tradingeconomics.com/markets/peers/aapl%3Aus%2Cindu%3Aind?c=TESTKEY"

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"peers": "raw"})
