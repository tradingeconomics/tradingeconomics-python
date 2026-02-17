import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getAllCountries
from tradingeconomics import glob


class TestGetAllCountries(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"countries": "all"}
    )
    def test_get_all_countries(self, mock_request):
        # Get all countries
        result = getAllCountries()

        expected_url = "/country/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"countries": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"countries": "df"}
    )
    def test_get_all_countries_with_output_type(self, mock_request):
        # Get all countries with output type
        result = getAllCountries(output_type="df")

        expected_url = "/country/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"countries": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"raw": "json", "countries": "data"},
    )
    def test_get_all_countries_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getAllCountries(output_type="raw")

        expected_url = "/country/"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "countries": "data"})
