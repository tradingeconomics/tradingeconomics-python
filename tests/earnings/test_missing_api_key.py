import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob
from tradingeconomics.earnings import LoginError


class TestMissingApiKey(unittest.TestCase):

    @patch.object(glob, "apikey", None)
    @patch("tradingeconomics.earnings.fn.dataRequest")
    def test_missing_api_key(self, mock_request):
        # When API key is missing, getEarnings must raise LoginError
        with self.assertRaises(LoginError):
            getEarnings(symbols="msft:us")
        # dataRequest must never be called
        mock_request.assert_not_called()
