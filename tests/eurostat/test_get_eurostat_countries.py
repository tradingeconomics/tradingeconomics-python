import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatCountries
from tradingeconomics import glob


class TestGetEurostatCountries(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"countries": "ok"})
    def test_get_eurostat_countries(self, mock_request):
        # Test getEurostatCountries function
        result = getEurostatCountries()

        expected_url = "/eurostat/countries"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"countries": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value=[{"country": "Denmark"}],
    )
    def test_get_eurostat_countries_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getEurostatCountries(output_type="df")

        expected_url = "/eurostat/countries"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"country": "Denmark"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest",
        return_value=[{"country": "Sweden"}],
    )
    def test_get_eurostat_countries_output_type_raw(self, mock_request):
        result = getEurostatCountries(output_type="raw")

        expected_url = "/eurostat/countries"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"country": "Sweden"}])
