import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "all"})
    def test_get_ipo_no_parameters(self, mock_request):
        # Get all IPO data
        result = getIpo()

        expected_url = "/ipo"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "all"})
