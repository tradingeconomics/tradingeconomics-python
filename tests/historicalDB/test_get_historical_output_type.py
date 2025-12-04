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

        expected_url = (
            "https://api.tradingeconomics.com/markets/historical/aapl%3Aus"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])
