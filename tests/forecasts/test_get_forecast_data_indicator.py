import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastData
from tradingeconomics import glob


class TestGetForecastDataIndicator(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest", return_value={"indicator": "ok"}
    )
    def test_forecast_indicator_single(self, mock_request):
        # Get forecast data for single indicator
        result = getForecastData(indicator="GDP Growth Rate")

        expected_url = "/forecast/indicator/GDP%20Growth%20Rate"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicator": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value={"indicator": "multiple"},
    )
    def test_forecast_indicator_multiple(self, mock_request):
        # Get forecast data for multiple indicators
        result = getForecastData(indicator=["Exports", "Imports"])

        expected_url = "/forecast/indicator/Exports%2CImports"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"indicator": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest", return_value=[{"indicator": "GDP"}]
    )
    def test_forecast_indicator_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getForecastData(indicator="GDP Growth Rate", output_type="df")

        expected_url = "/forecast/indicator/GDP%20Growth%20Rate"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"indicator": "GDP"}])
