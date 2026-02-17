import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalUpdates
from tradingeconomics import glob


class TestGetHistoricalUpdates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"updates": "ok"})
    def test_historical_updates(self, mock_request):
        # Get historical updates
        result = getHistoricalUpdates()

        expected_url = "/historical/updates"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest", return_value=[{"update": "data"}]
    )
    def test_historical_updates_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getHistoricalUpdates(output_type="df")

        expected_url = "/historical/updates"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"update": "data"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"raw": "json", "updates": "data"},
    )
    def test_historical_updates_output_type_raw(self, mock_request):
        # Test with output_type='raw' parameter
        result = getHistoricalUpdates(output_type="raw")

        expected_url = "/historical/updates"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "updates": "data"})
