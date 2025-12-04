import unittest
from unittest.mock import patch, MagicMock
from tradingeconomics.historicalDB import getHistorical
from tradingeconomics import glob
from datetime import datetime
from dateutil.relativedelta import relativedelta


class TestGetHistoricalEndDateOnly(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalDB.fn.dataRequest", return_value={"enddate": "ok"}
    )
    def test_historical_end_date_only(self, mock_request):
        # When only endDate is provided, initDate is auto-calculated as 1 month before
        result = getHistorical(symbol="aapl:us", endDate="2020-02-01")

        # initDate should be 2020-01-01 (1 month before endDate)
        expected_url = "https://api.tradingeconomics.com/markets/historical/aapl%3Aus?d1=2020-01-01&d2=2020-02-01&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"enddate": "ok"})
