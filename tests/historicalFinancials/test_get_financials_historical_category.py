import unittest
from unittest.mock import patch
from tradingeconomics.historicalFinancials import getFinancialsHistorical
from tradingeconomics import glob


class TestGetFinancialsHistoricalCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "ok"},
    )
    def test_financials_historical_category_with_space(self, mock_request):
        # Get historical financials data with category containing space
        result = getFinancialsHistorical(symbol="aapl:us", category="total assets")

        expected_url = "/financials/historical/aapl%3Aus%3Atotal-assets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "ok"})
