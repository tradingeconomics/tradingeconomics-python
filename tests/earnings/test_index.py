import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestIndex(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"index": "ok"})
    def test_index_parameter(self, mock_request, mock_dates):
        # Provide an index filter and ensure URL is built correctly
        result = getEarnings(index="ndx:ind")

        expected_url = (
            "https://api.tradingeconomics.com/earnings-revenues/index/ndx:ind"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"index": "ok"})
