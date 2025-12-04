import unittest
from unittest.mock import patch
from tradingeconomics.comtrade import getCmtTotalByType
from tradingeconomics import glob


class TestGetCmtTotalByType(unittest.TestCase):
    """
    Unit tests for getCmtTotalByType.
    Validates parameter checking, URL construction, and mocked dataRequest.
    """

    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_country(self, mock_request):
        result = getCmtTotalByType(country=None, type="import")
        self.assertEqual(result, "country is missing")
        mock_request.assert_not_called()

    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_type(self, mock_request):
        result = getCmtTotalByType(country="Portugal", type=None)
        self.assertEqual(result, "type is missing. Choose 'import' or 'export'")
        mock_request.assert_not_called()

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_valid_import(self, mock_request):
        result = getCmtTotalByType(country="Portugal", type="import")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/import/Portugal/totals/?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_valid_export(self, mock_request):
        result = getCmtTotalByType(country="Brazil", type="export")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/export/Brazil/totals/?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
