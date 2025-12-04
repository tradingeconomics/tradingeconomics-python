import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "country"})
    def test_get_ipo_by_country(self, mock_request):
        # Get IPO data for specific country
        result = getIpo(country="United States")

        expected_url = (
            "https://api.tradingeconomics.com/ipo/country/United%20States"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "countries"})
    def test_get_ipo_by_multiple_countries(self, mock_request):
        # Get IPO data for multiple countries
        result = getIpo(country=["United States", "Hong Kong"])

        expected_url = "https://api.tradingeconomics.com/ipo/country/United%20States,Hong%20Kong"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "countries"})
