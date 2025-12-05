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

    # --- Single country (requires date) ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="FINALURL")
    def test_single_country(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(country="mexico", initDate="2020-01-01")

        expected_start = "/credit-ratings/historical/country/mexico"

        mock_dates.assert_called_once_with(expected_start, "2020-01-01", None)
        mock_request.assert_called_once_with(api_request="FINALURL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- Multiple countries (requires date) ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="FINALURL")
    def test_multiple_countries(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country=["mexico", "sweden"], endDate="2023-12-31"
        )

        expected_start = "/credit-ratings/historical/country/mexico,sweden"

        mock_dates.assert_called_once_with(expected_start, None, "2023-12-31")
        mock_request.assert_called_once_with(api_request="FINALURL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- With dates ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch(
        "tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_WITH_DATES"
    )
    def test_with_dates(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country="mexico", initDate="2010-01-01", endDate="2011-01-01"
        )

        expected_base = "/credit-ratings/historical/country/mexico"

        mock_dates.assert_called_once_with(expected_base, "2010-01-01", "2011-01-01")
        mock_request.assert_called_once_with(
            api_request="URL_WITH_DATES", output_type=None
        )
        self.assertEqual(result, {"ok": True})

    # --- output_type tests ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value="DataFrame")
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_FINAL")
    def test_with_output_type_df(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country="mexico", initDate="2010-01-01", output_type="df"
        )

        expected_base = "/credit-ratings/historical/country/mexico"

        mock_dates.assert_called_once_with(expected_base, "2010-01-01", None)
        mock_request.assert_called_once_with(api_request="URL_FINAL", output_type="df")
        self.assertEqual(result, "DataFrame")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.credit_ratings.fn.dataRequest", return_value=[{"raw": "data"}]
    )
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_FINAL")
    def test_with_output_type_raw(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country="sweden", initDate="2020-01-01", output_type="raw"
        )

        expected_base = "/credit-ratings/historical/country/sweden"

        mock_dates.assert_called_once_with(expected_base, "2020-01-01", None)
        mock_request.assert_called_once_with(api_request="URL_FINAL", output_type="raw")
        self.assertEqual(result, [{"raw": "data"}])

    # --- only initDate (no endDate) ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_FINAL")
    def test_with_only_init_date(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(country="mexico", initDate="2010-01-01")

        expected_base = "/credit-ratings/historical/country/mexico"

        mock_dates.assert_called_once_with(expected_base, "2010-01-01", None)
        mock_request.assert_called_once_with(api_request="URL_FINAL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- only endDate (no initDate) ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_FINAL")
    def test_with_only_end_date(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(country="mexico", endDate="2011-01-01")

        expected_base = "/credit-ratings/historical/country/mexico"

        mock_dates.assert_called_once_with(expected_base, None, "2011-01-01")
        mock_request.assert_called_once_with(api_request="URL_FINAL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- country with spaces and dates ---
    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch("tradingeconomics.credit_ratings.fn.checkDates", return_value="URL_FINAL")
    def test_country_with_spaces_and_dates(self, mock_dates, mock_request):
        result = getHistoricalCreditRatings(
            country="United States", initDate="2010-01-01", endDate="2011-01-01"
        )

        expected_base = "/credit-ratings/historical/country/United%20States"

        mock_dates.assert_called_once_with(expected_base, "2010-01-01", "2011-01-01")
        mock_request.assert_called_once_with(api_request="URL_FINAL", output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- Country without dates raises ValueError ---
    def test_country_without_dates_raises_error(self):
        with self.assertRaises(ValueError) as context:
            getHistoricalCreditRatings(country="mexico")

        self.assertIn("initDate", str(context.exception))
        self.assertIn("endDate", str(context.exception))
        self.assertIn("Country alone is not supported", str(context.exception))


if __name__ == "__main__":
    unittest.main()
