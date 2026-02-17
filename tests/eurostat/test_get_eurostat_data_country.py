import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"country": "ok"})
    def test_country_parameter_single(self, mock_request):
        # Provide a single country and ensure URL is built correctly
        result = getEurostatData(country="Denmark")

        expected_url = "/eurostat/country/Denmark"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"country": "multiple"}
    )
    def test_country_parameter_multiple(self, mock_request):
        # Provide multiple countries and ensure URL is built correctly
        result = getEurostatData(country=["Denmark", "Sweden"])

        expected_url = "/eurostat/country/Denmark%2CSweden"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"country": "df"})
    def test_country_output_type_df(self, mock_request):
        result = getEurostatData(country="Denmark", output_type="df")

        expected_url = "/eurostat/country/Denmark"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"country": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"country": "raw"})
    def test_country_output_type_raw(self, mock_request):
        result = getEurostatData(country="Sweden", output_type="raw")

        expected_url = "/eurostat/country/Sweden"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"country": "raw"})
