import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestPrecedence(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.earnings.fn.checkDates", side_effect=lambda url, s, e: url)
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"precedence": "ok"})
    def test_symbols_take_precedence(self, mock_request, mock_dates):
        # Symbols must override all other filters
        result = getEarnings(symbols="msft:us", country="united states", index="sp500", sector="technology")

        expected_url = "https://api.tradingeconomics.com/earnings-revenues/symbol/msft:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"precedence": "ok"})