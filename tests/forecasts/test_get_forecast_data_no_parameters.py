import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastData
from tradingeconomics import glob


class TestGetForecastDataNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_forecast_no_parameters_raises_error(self):
        # When no parameters are provided, should raise ValueError
        with self.assertRaises(ValueError) as context:
            getForecastData()

        self.assertIn(
            "At least one of the parameters, country or indicator, needs to be supplied.",
            str(context.exception),
        )
