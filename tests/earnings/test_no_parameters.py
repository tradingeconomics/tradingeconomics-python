import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"ok": True})
    def test_no_parameters(self, mock_request, mock_dates):
        # When no filters are provided, earnings should call base URL + ?c=APIKEY
        result = getEarnings()

        # Base URL expected
        expected_url = "https://api.tradingeconomics.com/earnings-revenues?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})
