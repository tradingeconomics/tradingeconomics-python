import unittest
from unittest.mock import patch
from tradingeconomics.historicalEurostat import getHistoricalEurostat
from tradingeconomics import glob


class TestGetHistoricalEurostatID(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value={"historical": "ok"},
    )
    def test_historical_eurostat_single_id(self, mock_request):
        # Get historical Eurostat data for single ID
        result = getHistoricalEurostat(ID="24804")

        expected_url = "/eurostat/historical/24804"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalEurostat.fn.dataRequest",
        return_value={"historical": "multiple"},
    )
    def test_historical_eurostat_multiple_ids(self, mock_request):
        # Get historical Eurostat data for multiple IDs
        result = getHistoricalEurostat(ID=["24804", "24805"])

        expected_url = "/eurostat/historical/24804%2C24805"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"historical": "multiple"})
