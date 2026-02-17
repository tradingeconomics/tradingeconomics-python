import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarningsType, LoginError
from tradingeconomics import glob


class TestGetEarningsType(unittest.TestCase):

    @patch.object(glob, "apikey", None)
    @patch("tradingeconomics.earnings.fn.dataRequest")
    def test_missing_api_key(self, mock_request):
        # API key validation moved to dataRequest()
        mock_request.return_value = []
        getEarningsType(type="ipo")
        mock_request.assert_called_once()

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": "ipo"})
    def test_type_parameter(self, mock_request):
        result = getEarningsType(type="ipo")

        expected_url = "/earnings?type=ipo"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"type": "ipo"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": None})
    def test_no_type_parameter(self, mock_request):
        result = getEarningsType()

        expected_url = "/earnings?type="

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"type": None})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": "df"})
    def test_type_with_output_df(self, mock_request):
        result = getEarningsType(type="ipo", output_type="df")

        expected_url = "/earnings?type=ipo"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"type": "df"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": "raw"})
    def test_type_with_output_raw(self, mock_request):
        result = getEarningsType(type="dividend", output_type="raw")

        expected_url = "/earnings?type=dividend"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"type": "raw"})
