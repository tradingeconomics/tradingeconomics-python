import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url + f"&init={s}&end={e}")
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"dates": "ok"})
    def test_dates_are_applied(self, mock_request, mock_dates):
        # Provide date filters and ensure checkDates adjusts the URL
        result = getEarnings(initDate="2020-01-01", endDate="2020-12-31")

        base_url = "https://api.tradingeconomics.com/earnings-revenues?c=TESTKEY"
        expected_url = base_url + "&init=2020-01-01&end=2020-12-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"dates": "ok"})
