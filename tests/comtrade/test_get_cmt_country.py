# FILE: tests/comtrade/test_getCmtCountry.py
# Unit tests for getCmtCountry()
# - Tests URL generation
# - Tests page handling
# - Tests passthrough of fn.dataRequest

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtCountry


class TestGetCmtCountry(unittest.TestCase):

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_no_country(self, mock_dataRequest):
        """
        If country=None, URL should be:
        https://api.tradingeconomics.com/comtrade/countries?c=guest:guest
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtCountry(country=None)

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/countries?c=guest:guest"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_country_single(self, mock_dataRequest):
        """
        Single country string should generate:
        https://api.tradingeconomics.com/comtrade/country/<encoded>?c=...
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtCountry(country="portugal")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/portugal?c=guest:guest"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_multiple_countries(self, mock_dataRequest):
        """
        Multiple countries are joined with '/', then encoded:
        ["portugal","spain"] -> "portugal/spain" -> encoded
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtCountry(country=["portugal", "spain"])

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/portugal/spain?c=guest:guest"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_country_with_page(self, mock_dataRequest):
        """
        Page number should be appended as /<page> before ?c=apikey
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtCountry(country="china", page_number=3)

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/china/3?c=guest:guest"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()