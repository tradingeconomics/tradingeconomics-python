import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob
from tradingeconomics.earnings import LoginError


class TestMissingApiKey(unittest.TestCase):

    @patch.object(glob, "apikey", None)
    @patch("tradingeconomics.earnings.fn.dataRequest")
    def test_missing_api_key(self, mock_request):
        # API key validation moved to dataRequest()
        mock_request.return_value = []
        getEarnings(symbols="msft:us")
        # dataRequest is called (it handles missing API key)
        mock_request.assert_called_once()
