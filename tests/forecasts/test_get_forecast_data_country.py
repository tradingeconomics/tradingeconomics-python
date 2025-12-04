import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastData
from tradingeconomics import glob


class TestGetForecastDataCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"country": "ok"})
    def test_forecast_country_single(self, mock_request):
        # Get forecast data for single country
        result = getForecastData(country="United States")

        expected_url = "https://api.tradingeconomics.com/forecast/country/United%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value={"country": "multiple"},
    )
    def test_forecast_country_multiple(self, mock_request):
        # Get forecast data for multiple countries
        result = getForecastData(country=["United States", "India"])

        expected_url = "https://api.tradingeconomics.com/forecast/country/United%20States%2CIndia"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value=[{"country": "United States"}],
    )
    def test_forecast_country_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getForecastData(country="United States", output_type="df")

        expected_url = "https://api.tradingeconomics.com/forecast/country/United%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"country": "United States"}])
