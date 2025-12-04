import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastByTicker
from tradingeconomics import glob


class TestGetForecastByTickerNoParameter(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_forecast_ticker_no_parameter(self):
        # When no ticker is provided, should return error message
        result = getForecastByTicker()

        self.assertEqual(result, "Ticker is required")
