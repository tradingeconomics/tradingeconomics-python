import unittest
from unittest.mock import patch
from tradingeconomics.historicalMarkets import fetchMarkets
from tradingeconomics import glob


class TestFetchMarketsOutputType(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_fetch_markets_with_output_type_df(self, mock_request):
        # Test with output_type='df'
        result = fetchMarkets(symbol="indu:ind", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/markets/historical/indu%3Aind"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_fetch_markets_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = fetchMarkets(symbol="indu:ind", output_type="raw")

        expected_url = (
            "https://api.tradingeconomics.com/markets/historical/indu%3Aind"
        )

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"value": 100}])
