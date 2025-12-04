import unittest
from unittest.mock import patch
from tradingeconomics.dividends import getDividends
from tradingeconomics import glob


class TestGetDividends(unittest.TestCase):

    # -----------------------
    # API KEY MISSING
    # -----------------------
    @patch("tradingeconomics.dividends.fn.dataRequest")
    @patch.object(glob, "apikey", None)
    def test_missing_api_key(self, mock_request):
        with self.assertRaises(Exception):
            getDividends(symbols="msft:us")
        mock_request.assert_not_called()

    # -----------------------
    # NO PARAMETERS
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_no_parameters(self, mock_request, mock_dates):
        result = getDividends()

        expected_url = "https://api.tradingeconomics.com/dividends?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # SINGLE SYMBOL
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_single_symbol(self, mock_request, mock_dates):
        result = getDividends(symbols="msft:us")

        expected_url = (
            "https://api.tradingeconomics.com/dividends/symbol/msft:us?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # MULTIPLE SYMBOLS
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_multiple_symbols(self, mock_request, mock_dates):
        result = getDividends(symbols=["msft:us", "aapl:us"])

        expected_url = "https://api.tradingeconomics.com/dividends/symbol/msft:us,aapl:us?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # WITH DATES
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&from={s}&to={e}",
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_dates(self, mock_request, mock_dates):
        result = getDividends(
            symbols="msft:us", startDate="2020-01-01", endDate="2021-01-01"
        )

        expected_url = (
            "https://api.tradingeconomics.com/dividends/symbol/msft:us?c=TESTKEY"
            "&from=2020-01-01&to=2021-01-01"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
