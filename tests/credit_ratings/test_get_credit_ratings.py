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

        expected_url = "/credit-ratings"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- single country ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_single_country(self, mock_request):
        result = getCreditRatings(country="sweden")

        expected_url = "/credit-ratings/country/sweden"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- multiple countries ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_multiple_countries(self, mock_request):
        result = getCreditRatings(country=["mexico", "sweden"])

        expected_url = "/credit-ratings/country/mexico,sweden"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    # --- missing API key now handled by dataRequest() ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest")
    @patch.object(glob, "apikey", None)
    def test_missing_api_key(self, mock_request):
        # API key validation moved to dataRequest(), so function still calls it
        mock_request.return_value = []

        getCreditRatings(country="sweden")

        # Verify dataRequest was called (it will handle missing API key)
        mock_request.assert_called_once()

    # --- output_type tests ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value="DataFrame")
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_output_type_df(self, mock_request):
        result = getCreditRatings(country="sweden", output_type="df")

        expected_url = "/credit-ratings/country/sweden"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "DataFrame")

    @patch(
        "tradingeconomics.credit_ratings.fn.dataRequest", return_value=[{"raw": "data"}]
    )
    @patch.object(glob, "apikey", "TESTKEY")
    def test_with_output_type_raw(self, mock_request):
        result = getCreditRatings(country="mexico", output_type="raw")

        expected_url = "/credit-ratings/country/mexico"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"raw": "data"}])

    # --- country with spaces (URL encoding) ---
    @patch("tradingeconomics.credit_ratings.fn.dataRequest", return_value={"ok": True})
    @patch.object(glob, "apikey", "TESTKEY")
    def test_country_with_spaces(self, mock_request):
        result = getCreditRatings(country="United States")

        expected_url = "/credit-ratings/country/United%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()
