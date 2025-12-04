import unittest
from unittest.mock import patch
from tradingeconomics.earnings import getEarnings
from tradingeconomics import glob


class TestDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.earnings.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&init={s}&end={e}",
    )
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"dates": "ok"})
    def test_dates_are_applied(self, mock_request, mock_dates):
        # Provide date filters and ensure checkDates adjusts the URL
        result = getEarnings(initDate="2020-01-01", endDate="2020-12-31")

        base_url = "/earnings-revenues"
        expected_url = base_url + "&init=2020-01-01&end=2020-12-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"dates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.earnings.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&init={s}&end={e}",
    )
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"dates": "ok"})
    def test_symbols_with_dates_and_df(self, mock_request, mock_dates):
        result = getEarnings(
            symbols="msft:us",
            initDate="2020-01-01",
            endDate="2020-12-31",
            output_type="df",
        )

        expected_url = (
            "/earnings-revenues/symbol/msft:us&init=2020-01-01&end=2020-12-31"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"dates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.earnings.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&init={s}" if s and not e else url,
    )
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"dates": "ok"})
    def test_only_init_date(self, mock_request, mock_dates):
        result = getEarnings(symbols="aapl:us", initDate="2020-01-01")

        expected_url = "/earnings-revenues/symbol/aapl:us&init=2020-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"dates": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.earnings.fn.checkDates",
        side_effect=lambda url, s, e: url + f"&end={e}" if e and not s else url,
    )
    @patch("tradingeconomics.earnings.fn.dataRequest", return_value={"dates": "ok"})
    def test_only_end_date(self, mock_request, mock_dates):
        result = getEarnings(symbols="googl:us", endDate="2020-12-31")

        expected_url = "/earnings-revenues/symbol/googl:us&end=2020-12-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"dates": "ok"})
