import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"country": "ok"})
    def test_country_parameter(self, mock_request, mock_dates):
        # Provide a country filter and ensure URL is built correctly
        result = getEarnings(country="united states")

        expected_url = "https://api.tradingeconomics.com/earnings-revenues/country/united%20states?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})