import unittest
from unittest.mock import patch
from tradingeconomics.historicalMarkets import fetchMarkets
from tradingeconomics import glob


class TestFetchMarketsSymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "ok"},
    )
    def test_fetch_markets_single_symbol(self, mock_request):
        # Get historical markets data for single symbol
        result = fetchMarkets(symbol="indu:ind")

        expected_url = "/markets/historical/indu%3Aind"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value={"markets": "multiple"},
    )
    def test_fetch_markets_multiple_symbols(self, mock_request):
        # Get historical markets data for multiple symbols
        result = fetchMarkets(symbol=["aapl:us", "indu:ind"])

        expected_url = "/markets/historical/aapl%3Aus%2Cindu%3Aind"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"markets": "multiple"})
