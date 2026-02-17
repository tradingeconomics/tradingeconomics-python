import unittest
from unittest.mock import patch
from tradingeconomics.historicalFinancials import getFinancialsHistorical
from tradingeconomics import glob


class TestGetFinancialsHistoricalSymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "ok"},
    )
    def test_financials_historical_single_symbol_single_category(self, mock_request):
        # Get historical financials data for single symbol and category
        result = getFinancialsHistorical(symbol="aapl:us", category="assets")

        expected_url = "/financials/historical/aapl%3Aus%3Aassets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "multiple"},
    )
    def test_financials_historical_multiple_symbols(self, mock_request):
        # Get historical financials data for multiple symbols and single category
        result = getFinancialsHistorical(
            symbol=["aapl:us", "tsla:us"], category="assets"
        )

        expected_url = "/financials/historical/aapl%3Aus%3Aassets%2Ctsla%3Aus%3Aassets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "categories"},
    )
    def test_financials_historical_multiple_categories(self, mock_request):
        # Get historical financials data for single symbol and multiple categories
        result = getFinancialsHistorical(symbol="aapl:us", category=["assets", "debt"])

        expected_url = "/financials/historical/aapl%3Aus%3Aassets%2Caapl%3Aus%3Adebt"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "both"},
    )
    def test_financials_historical_multiple_symbols_and_categories(self, mock_request):
        # Get historical financials data for multiple symbols and categories
        result = getFinancialsHistorical(
            symbol=["aapl:us", "tsla:us"], category=["assets", "debt"]
        )

        expected_url = "/financials/historical/aapl%3Aus%3Aassets%2Caapl%3Aus%3Adebt%2Ctsla%3Aus%3Aassets%2Ctsla%3Aus%3Adebt"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "both"})
