import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoOutputType(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value=[{"value": 100}])
    def test_get_ipo_with_output_type_df(self, mock_request):
        # Test with output_type='df'
        result = getIpo(output_type="df")

        expected_url = "/ipo"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value=[{"value": 100}])
    def test_get_ipo_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getIpo(ticker="SWIN", output_type="raw")

        expected_url = "/ipo/ticker/SWIN"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"value": 100}])
