import unittest
from unittest.mock import patch
from tradingeconomics.comtrade import getCmtCountryFilterByType
from tradingeconomics import glob


class TestGetCmtCountryFilterByType(unittest.TestCase):
    """
    Unit tests for getCmtCountryFilterByType.
    Validates required parameters, URL formation, country1/country2 logic,
    adding &type=, and mocked dataRequest.
    """

    # --- missing parameters ---
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_country1(self, mock_request):
        result = getCmtCountryFilterByType(country1=None, country2="Spain", type="import")
        self.assertEqual(result, "country is missing")
        mock_request.assert_not_called()

    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_type(self, mock_request):
        result = getCmtCountryFilterByType(country1="Portugal", country2=None, type=None)
        self.assertEqual(result, "type is missing. Choose 'import' or 'export'")
        mock_request.assert_not_called()

    # --- only country1 ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_only_country1(self, mock_request):
        result = getCmtCountryFilterByType(country1="Portugal", country2=None, type="import")
    
        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/Portugal?type=import"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- two countries ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_two_countries(self, mock_request):
        result = getCmtCountryFilterByType(country1="Portugal", country2="Spain", type="export")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/Portugal/Spain?type=export"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
