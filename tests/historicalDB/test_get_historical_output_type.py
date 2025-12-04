import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalOutputType(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value=[{"value": 100}]
    )
    def test_historical_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getHistorical(symbol="aapl:us", output_type="df")

        expected_url = "/markets/historical/aapl%3Aus"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"raw": "json", "symbol": "aapl:us"},
    )
    def test_historical_with_output_type_raw(self, mock_request):
        # Test with output_type='raw' parameter
        result = getHistorical(symbol="aapl:us", output_type="raw")

        expected_url = "/markets/historical/aapl%3Aus"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "symbol": "aapl:us"})
