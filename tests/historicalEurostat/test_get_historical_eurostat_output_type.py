import unittest
from unittest.mock import patch
from tradingeconomics.historicalEurostat import getHistoricalEurostat
from tradingeconomics import glob


class TestGetHistoricalEurostatOutputType(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_historical_eurostat_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getHistoricalEurostat(ID="24804", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/eurostat/historical/24804?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_historical_eurostat_raw_output(self, mock_request):
        # Test with raw output_type
        result = getHistoricalEurostat(ID="24804", output_type="raw")

        expected_url = (
            "https://api.tradingeconomics.com/eurostat/historical/24804?c=TESTKEY"
        )

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"value": 100}])
