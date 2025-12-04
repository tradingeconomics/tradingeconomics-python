import unittest
from unittest.mock import patch
from tradingeconomics.financials import getSectors
from tradingeconomics import glob


class TestGetSectors(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.financials.fn.checkDates", side_effect=lambda url: url)
    @patch("tradingeconomics.financials.fn.dataRequest", return_value={"sectors": "ok"})
    def test_get_sectors(self, mock_request, mock_check_dates):
        # Get all sectors
        result = getSectors()

        expected_url = "/sectors/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"sectors": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.financials.fn.checkDates", side_effect=lambda url: url)
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"sector": "Technology"}],
    )
    def test_get_sectors_with_output_type(self, mock_request, mock_check_dates):
        # Test with output_type parameter
        result = getSectors(output_type="df")

        expected_url = "/sectors/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"sector": "Technology"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.financials.fn.checkDates", side_effect=lambda url: url)
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"sector": "Finance"}],
    )
    def test_get_sectors_output_type_raw(self, mock_request, mock_check_dates):
        result = getSectors(output_type="raw")

        expected_url = "/sectors/"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"sector": "Finance"}])
