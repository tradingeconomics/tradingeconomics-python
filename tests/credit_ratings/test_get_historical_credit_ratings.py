import unittest
from unittest.mock import patch
from tradingeconomics.credit_ratings import getHistoricalCreditRatings
from tradingeconomics import glob


class TestGetHistoricalCreditRatings(unittest.TestCase):
    """
    Unit tests for getHistoricalCreditRatings().
    """

    # --- No parameters at all ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="APPENDED")
    def test_no_params(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings()

        mock_dates.assert_called_once()
        mock_request.assert_called_once_with(api_request="APPENDED", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- Single country ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="FINALURL")
    def test_single_country(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(country="mexico")

        expected_start = (
            "https://api.tradingeconomics.com/credit-ratings/historical/country/mexico"
        )

        mock_dates.assert_called_once_with(expected_start, None, None)
        mock_request.assert_called_once_with(api_request="FINALURL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- Multiple countries ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="FINALURL")
    def test_multiple_countries(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(country=["mexico", "sweden"])

        expected_start = (
            "https://api.tradingeconomics.com/credit-ratings/historical/country/mexico,sweden"
        )

        mock_dates.assert_called_once_with(expected_start, None, None)
        mock_request.assert_called_once_with(api_request="FINALURL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- With dates ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_WITH_DATES")
    def test_with_dates(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country="mexico",
            initDate="2010-01-01",
            endDate="2011-01-01"
        )

        expected_base = (
            "https://api.tradingeconomics.com/credit-ratings/historical/country/mexico"
        )

        mock_dates.assert_called_once_with(expected_base, "2010-01-01", "2011-01-01")
        mock_request.assert_called_once_with(api_request="URL_WITH_DATES", output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
