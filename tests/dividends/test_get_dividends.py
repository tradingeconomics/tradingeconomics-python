import unittest
from unittest.mock import patch
from tradingeconomics.dividends import getDividends
from tradingeconomics import glob


class TestGetDividends(unittest.TestCase):

    # -----------------------
    # API KEY MISSING - now handled by dataRequest()
    # -----------------------
    @patch("tradingeconomics.dividends.fn.dataRequest")
    @patch.object(glob, "apikey", None)
    def test_missing_api_key(self, mock_request):
        mock_request.return_value = []
        getDividends(symbols="msft:us")
        mock_request.assert_called_once()

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

        expected_url = "/dividends"

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

        expected_url = "/dividends/symbol/msft:us"

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

        expected_url = "/dividends/symbol/msft:us,aapl:us"

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

        expected_url = "/dividends/symbol/msft:us" "&from=2020-01-01&to=2021-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # OUTPUT TYPE - DATAFRAME
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_output_type_df(self, mock_request, mock_dates):
        result = getDividends(symbols="aapl:us", output_type="df")

        expected_url = "/dividends/symbol/aapl:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # OUTPUT TYPE - RAW
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_output_type_raw(self, mock_request, mock_dates):
        result = getDividends(symbols="msft:us", output_type="raw")

        expected_url = "/dividends/symbol/msft:us"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # ONLY START DATE
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&from={s}" if s and not e else url,
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_only_start_date(self, mock_request, mock_dates):
        result = getDividends(symbols="msft:us", startDate="2020-01-01")

        expected_url = "/dividends/symbol/msft:us&from=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # ONLY END DATE
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&to={e}" if e and not s else url,
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_only_end_date(self, mock_request, mock_dates):
        result = getDividends(symbols="aapl:us", endDate="2021-12-31")

        expected_url = "/dividends/symbol/aapl:us&to=2021-12-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # SYMBOL WITH SPECIAL CHARACTERS
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_symbol_with_special_chars(self, mock_request, mock_dates):
        # stringOrList should preserve colons in ticker symbols
        result = getDividends(symbols="BRK.B:US")

        expected_url = "/dividends/symbol/BRK.B:US"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # SINGLE SYMBOL AS LIST
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates", side_effect=lambda url, s, e: url
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_single_symbol_as_list(self, mock_request, mock_dates):
        # Test that single symbol in list is handled correctly
        result = getDividends(symbols=["msft:us"])

        expected_url = "/dividends/symbol/msft:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # -----------------------
    # MULTIPLE SYMBOLS WITH DATES AND DATAFRAME
    # -----------------------
    @patch(
        "tradingeconomics.dividends.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&from={s}&to={e}",
    )
    @patch("tradingeconomics.dividends.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_multiple_symbols_with_dates_df(self, mock_request, mock_dates):
        result = getDividends(
            symbols=["msft:us", "aapl:us", "googl:us"],
            startDate="2020-01-01",
            endDate="2021-01-01",
            output_type="df",
        )

        expected_url = (
            "/dividends/symbol/msft:us,aapl:us,googl:us&from=2020-01-01&to=2021-01-01"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
