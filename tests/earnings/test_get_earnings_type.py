import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarningsType, LoginError
from tradingeconomics import glob


class TestGetEarningsType(unittest.TestCase):

    @patch.object(glob, "apikey", None)
    @patch("tradingeconomics.earnings.fn.dataRequest")
    def test_missing_api_key(self, mock_request):
        # Missing API key must raise LoginError
        with self.assertRaises(LoginError):
            getEarningsType(type="ipo")
        mock_request.assert_not_called()

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": "ipo"})
    def test_type_parameter(self, mock_request):
        result = getEarningsType(type="ipo")

        expected_url = "https://api.tradingeconomics.com/earnings?type=ipo&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"type": "ipo"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"type": None})
    def test_no_type_parameter(self, mock_request):
        result = getEarningsType()

        expected_url = "https://api.tradingeconomics.com/earnings?type=&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"type": None})