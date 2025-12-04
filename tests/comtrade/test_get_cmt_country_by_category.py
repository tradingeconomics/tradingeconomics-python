import unittest
from unittest.mock import patch
from tradingeconomics.comtrade import getCmtCountryByCategory
from tradingeconomics import glob

class TestGetCmtCountryByCategory(unittest.TestCase):

    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_missing_country(self, mock_request):
        result = getCmtCountryByCategory(country=None, type="import")
        self.assertEqual(result, "country is missing")
        mock_request.assert_not_called()

    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_missing_type(self, mock_request):
        result = getCmtCountryByCategory(country="Portugal", type=None)
        self.assertEqual(result, "type is missing. Choose 'import' or 'export'")
        mock_request.assert_not_called()

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_no_category(self, mock_request):
        result = getCmtCountryByCategory(country="Portugal", type="import", category=None)

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/import/Portugal"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_with_category(self, mock_request):
        result = getCmtCountryByCategory(country="United States", type="export", category="live animals")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/export/United%20States/live%20animals"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == '__main__':
    unittest.main()
