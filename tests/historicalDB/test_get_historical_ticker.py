import unittest
from unittest.mock import patch
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob


class TestGetHistoricalTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value={"ticker": "ok"}
    )
    def test_historical_ticker_no_colon(self, mock_request):
        # Get historical data for ticker without colon
        result = getHistorical(symbol="USURTOT")

        expected_url = (
            "https://api.tradingeconomics.com/historical/ticker/USURTOT?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalDB.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest",
        return_value={"ticker": "with_date"},
    )
    def test_historical_ticker_with_init_date(self, mock_request, mock_validate):
        # Get historical data for ticker with init date
        result = getHistorical(symbol="USURTOT", initDate="2015-01-01")

        expected_url = "https://api.tradingeconomics.com/historical/ticker/USURTOT/2015-01-01?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ticker": "with_date"})
