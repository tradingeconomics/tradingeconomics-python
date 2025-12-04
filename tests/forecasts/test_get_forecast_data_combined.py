import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastData
from tradingeconomics import glob


class TestGetForecastDataCombined(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"combined": "ok"})
    def test_forecast_country_and_indicator(self, mock_request):
        # Get forecast data for country and indicator
        result = getForecastData(country="United States", indicator="Imports")

        expected_url = "https://api.tradingeconomics.com/forecast/country/United%20States/indicator/Imports?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"combined": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value={"combined": "multiple"},
    )
    def test_forecast_multiple_country_and_indicator(self, mock_request):
        # Get forecast data for multiple countries and indicators
        result = getForecastData(
            country=["United States", "India"], indicator=["Imports", "Exports"]
        )

        expected_url = "https://api.tradingeconomics.com/forecast/country/United%20States%2CIndia/indicator/Imports%2CExports?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"combined": "multiple"})
