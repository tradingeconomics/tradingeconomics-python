import unittest
from unittest.mock import patch
from tradingeconomics.comtrade import getCmtSnapshotByType
from tradingeconomics import glob


class TestGetCmtSnapshotByType(unittest.TestCase):
    """
    Unit tests for getCmtSnapshotByType.
    Validates:
    - required parameters
    - URL construction
    - mock of dataRequest
    - encoding of country
    """

    # Missing country
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_country(self, mock_request):
        with self.assertRaises(Exception):
            getCmtSnapshotByType(country=None, type="import")
        mock_request.assert_not_called()

    # Missing type
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_missing_type(self, mock_request):
        with self.assertRaises(Exception):
            getCmtSnapshotByType(country="Portugal", type=None)
        mock_request.assert_not_called()

    # Valid import
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_valid_import(self, mock_request):
        result = getCmtSnapshotByType(country="Portugal", type="import")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/Portugal?type=import"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # Valid export with special characters
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.comtrade.fn.dataRequest", return_value={"ok": True})
    def test_valid_export_encoded(self, mock_request):
        result = getCmtSnapshotByType(country="United States", type="export")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/country/United%20States?type=export"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
