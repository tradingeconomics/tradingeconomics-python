import unittest
from unittest.mock import patch
from tradingeconomics.forecasts import getForecastUpdates
from tradingeconomics import glob


class TestGetForecastUpdates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"updates": "ok"})
    def test_forecast_updates_no_parameters(self, mock_request):
        # Get all forecast updates
        result = getForecastUpdates()

        expected_url = "/forecast/updates"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"updates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.stringOrList", return_value="france")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"country": "ok"})
    def test_forecast_updates_country_single(self, mock_request, mock_string_or_list):
        # Get forecast updates for single country
        result = getForecastUpdates(country="france")

        expected_url = "/forecast/updates?country=france"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.stringOrList", return_value="france%2Csweden")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest",
        return_value={"country": "multiple"},
    )
    def test_forecast_updates_country_multiple(self, mock_request, mock_string_or_list):
        # Get forecast updates for multiple countries
        result = getForecastUpdates(country=["france", "sweden"])

        expected_url = "/forecast/updates?country=france%2Csweden"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.forecasts.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.forecasts.fn.stringOrList", return_value="mexico")
    @patch("tradingeconomics.forecasts.fn.dataRequest", return_value={"date": "ok"})
    def test_forecast_updates_with_date(
        self, mock_request, mock_string_or_list, mock_validate
    ):
        # Get forecast updates with init_date
        result = getForecastUpdates(country="mexico", init_date="2024-11-15")

        expected_url = "/forecast/updates?country=mexico&date=2024-11-15"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"date": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.forecasts.fn.dataRequest", return_value=[{"update": "data"}]
    )
    def test_forecast_updates_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getForecastUpdates(output_type="df")

        expected_url = "/forecast/updates"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"update": "data"}])
