# FILE: tests/comtrade/test_getCmtTwoCountries.py
# Unit tests for getCmtTwoCountries()
# - Tests URL generation for 1 or 2 countries
# - Tests pagination
# - Tests passthrough of fn.dataRequest

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtTwoCountries


class TestGetCmtTwoCountries(unittest.TestCase):

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_second_country(self, mock_dataRequest):
        """
        If only country1 is provided and country2=None, URL should be:
        https://api.tradingeconomics.com/comtrade/country/country1
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtTwoCountries(country1="portugal", country2=None)

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/portugal"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_two_countries(self, mock_dataRequest):
        """
        If both countries are provided, URL should be:
        https://api.tradingeconomics.com/comtrade/country/<c1>/<c2>
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtTwoCountries(country1="portugal", country2="spain")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/portugal/spain"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_two_countries_with_page(self, mock_dataRequest):
        """
        Page number must be appended at the end.
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtTwoCountries(country1="portugal", country2="spain", page_number=4)

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/portugal/spain/4"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()