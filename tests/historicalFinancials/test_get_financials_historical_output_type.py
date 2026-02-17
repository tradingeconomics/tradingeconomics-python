import unittest
from unittest.mock import patch
from tradingeconomics.historicalFinancials import getFinancialsHistorical
from tradingeconomics import glob


class TestGetFinancialsHistoricalOutputType(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_financials_historical_with_output_type_df(self, mock_request):
        # Test with output_type='df'
        result = getFinancialsHistorical(
            symbol="aapl:us", category="assets", output_type="df"
        )

        expected_url = "/financials/historical/aapl%3Aus%3Aassets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value=[{"value": 100}],
    )
    def test_financials_historical_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getFinancialsHistorical(
            symbol="aapl:us", category="assets", output_type="raw"
        )

        expected_url = "/financials/historical/aapl%3Aus%3Aassets"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"value": 100}])
