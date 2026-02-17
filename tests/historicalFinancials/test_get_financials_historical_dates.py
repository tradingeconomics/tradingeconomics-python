import unittest
from unittest.mock import patch
from tradingeconomics.historicalFinancials import getFinancialsHistorical
from tradingeconomics import glob


class TestGetFinancialsHistoricalDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalFinancials.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "with_init"},
    )
    def test_financials_historical_with_init_date(self, mock_request, mock_validate):
        # Get historical financials data with init date only
        result = getFinancialsHistorical(
            symbol="aapl:us", category="assets", initDate="2023-01-01"
        )

        expected_url = "/financials/historical/aapl%3Aus%3Aassets?d1=2023-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "with_init"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalFinancials.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalFinancials.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalFinancials.fn.dataRequest",
        return_value={"financials": "with_dates"},
    )
    def test_financials_historical_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical financials data with date range
        result = getFinancialsHistorical(
            symbol="aapl:us",
            category="assets",
            initDate="2023-01-01",
            endDate="2023-12-31",
        )

        expected_url = (
            "/financials/historical/aapl%3Aus%3Aassets?d1=2023-01-01&d2=2023-12-31"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"financials": "with_dates"})
