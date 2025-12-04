import unittest
from unittest.mock import patch
from tradingeconomics.credit_ratings import getCreditRatings
from tradingeconomics import glob


class TestGetCreditRatings(unittest.TestCase):
    """
    Unit tests for getCreditRatings().
    """

    # --- country=None ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_no_country(self, mock_request):
        result = getCreditRatings(country=None)

        expected_url = "https://api.tradingeconomics.com/credit-ratings?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- single country ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_single_country(self, mock_request):
        result = getCreditRatings(country="sweden")

        expected_url = (
            "https://api.tradingeconomics.com/credit-ratings/country/sweden?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- multiple countries ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_multiple_countries(self, mock_request):
        result = getCreditRatings(country=["mexico", "sweden"])

        expected_url = (
            "https://api.tradingeconomics.com/credit-ratings/country/mexico,sweden?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- missing API key ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest")
    @patch.object(glob, "apikey", None)
    def test_missing_api_key(self, mock_request):
        from tradingeconomics.credit_ratings import LoginError

        with self.assertRaises(LoginError):
            getCreditRatings(country="sweden")

        mock_request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
