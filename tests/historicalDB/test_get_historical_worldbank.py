import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalWorldBank(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value={"worldbank": "ok"}
    )
    def test_historical_worldbank_symbol(self, mock_request):
        # Get historical data for World Bank symbol
        result = getHistorical(symbol="are.fr.inr.rinr:worldbank")

        expected_url = "https://api.tradingeconomics.com/worldBank/historical?s=are.fr.inr.rinr"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"worldbank": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historicalDB.fn.validatePeriod")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"worldbank": "with_dates"},
    )
    def test_historical_worldbank_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get historical data for World Bank with date range
        result = getHistorical(
            symbol="are.fr.inr.rinr:worldbank",
            initDate="2010-01-01",
            endDate="2020-01-01",
        )

        expected_url = "https://api.tradingeconomics.com/worldBank/historical?s=are.fr.inr.rinr&d1=2010-01-01&d2=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"worldbank": "with_dates"})
