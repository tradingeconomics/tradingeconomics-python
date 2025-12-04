import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalComtrade(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value={"comtrade": "ok"}
    )
    def test_historical_comtrade_symbol(self, mock_request):
        # Get historical data for Comtrade symbol
        result = getHistorical(symbol="PRTESP24031:comtrade")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/historical/PRTESP24031?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"comtrade": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalDB.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"comtrade": "with_dates"},
    )
    def test_historical_comtrade_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical data for Comtrade with date range
        result = getHistorical(
            symbol="PRTESP24031:comtrade", initDate="2015-01-01", endDate="2020-01-01"
        )

        expected_url = "https://api.tradingeconomics.com/comtrade/historical/PRTESP24031?d1=2015-01-01&d2=2020-01-01&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"comtrade": "with_dates"})
