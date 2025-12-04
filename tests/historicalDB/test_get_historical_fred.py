import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalFred(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.dataRequest", return_value={"fred": "ok"})
    def test_historical_fred_symbol(self, mock_request):
        # Get historical data for FRED symbol
        result = getHistorical(symbol="RACEDISPARITY005007:fred")

        expected_url = "https://api.tradingeconomics.com/fred/historical/RACEDISPARITY005007"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"fred": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalDB.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"fred": "with_dates"},
    )
    def test_historical_fred_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical data for FRED with date range
        result = getHistorical(
            symbol="RACEDISPARITY005007:fred",
            initDate="2015-01-01",
            endDate="2020-01-01",
        )

        expected_url = "https://api.tradingeconomics.com/fred/historical/RACEDISPARITY005007?d1=2015-01-01&d2=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"fred": "with_dates"})
