import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalByTicker
from tradingeconomics import glob
from tradingeconomics.historical import ParametersError


class TestGetHistoricalByTickerErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_historical_by_ticker_no_ticker(self):
        # Should return error message when no ticker provided
        result = getHistoricalByTicker()

        self.assertEqual(result, "Ticker is required")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="USURTOT")
    def test_historical_by_ticker_end_date_without_start(
        self, mock_string_or_list, mock_validate
    ):
        # Should raise ParametersError when end_date provided without start_date
        with self.assertRaises(ParametersError) as context:
            getHistoricalByTicker(ticker="USURTOT", end_date="2015-09-30")

        self.assertIn(
            "start_date is required if end_date is provided", str(context.exception)
        )
