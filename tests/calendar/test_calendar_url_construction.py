"""
Unit tests for calendar.py URL construction
Tests that query parameters (importance, values) are correctly formatted with ? instead of &
"""

import unittest
from unittest.mock import patch, MagicMock
import tradingeconomics as te


class TestCalendarURLConstruction(unittest.TestCase):
    """Test that calendar API URLs are constructed correctly"""

    @patch("tradingeconomics.functions.dataRequest")
    def test_importance_only_uses_question_mark(self, mock_request):
        """Test that importance parameter alone uses ? not &"""
        mock_request.return_value = []

        te.getCalendarData(importance="2")

        # Get the URL that was passed to dataRequest
        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar?importance=2, not /calendar&importance=2
        self.assertIn(
            "?importance=2",
            called_url,
            f"Expected '?importance=2' in URL, got: {called_url}",
        )
        self.assertNotIn(
            "&importance=2",
            called_url.split("?")[0],
            f"Should not have '&importance=2' before '?', got: {called_url}",
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_values_only_uses_question_mark(self, mock_request):
        """Test that values parameter alone uses ? not &"""
        mock_request.return_value = []

        te.getCalendarData(values=True)

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar?values=true, not /calendar&values=true
        self.assertIn(
            "?values=true",
            called_url,
            f"Expected '?values=true' in URL, got: {called_url}",
        )
        self.assertNotIn(
            "&values=true",
            called_url.split("?")[0],
            f"Should not have '&values=true' before '?', got: {called_url}",
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_importance_and_values_uses_ampersand(self, mock_request):
        """Test that multiple query params use & between them"""
        mock_request.return_value = []

        te.getCalendarData(importance="3", values=True)

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar?importance=3&values=true
        self.assertIn("?", called_url, f"Expected '?' in URL, got: {called_url}")
        self.assertIn("importance=3", called_url)
        self.assertIn("values=true", called_url)

        # Check that & is used between parameters
        query_string = called_url.split("?")[1] if "?" in called_url else ""
        self.assertIn(
            "&", query_string, f"Expected '&' between query params, got: {called_url}"
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_country_with_importance_combines_correctly(self, mock_request):
        """Test that path params + query params are combined correctly"""
        mock_request.return_value = []

        te.getCalendarData(country="united states", importance="2")

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar/country/united%20states?importance=2
        expected_url = "/calendar/country/united%20states?importance=2"
        self.assertEqual(
            called_url, expected_url, f"Expected '{expected_url}', got: {called_url}"
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_country_with_importance_3_exact_url(self, mock_request):
        """Test exact URL format for country + importance=3 (regression test)"""
        mock_request.return_value = []

        te.getCalendarData(country="united states", importance="3")

        called_url = mock_request.call_args[1]["api_request"]

        # Should be exactly /calendar/country/united%20states?importance=3
        expected_url = "/calendar/country/united%20states?importance=3"
        self.assertEqual(
            called_url, expected_url, f"Expected '{expected_url}', got: {called_url}"
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_category_with_importance_combines_correctly(self, mock_request):
        """Test that category + importance uses correct format"""
        mock_request.return_value = []

        te.getCalendarData(category="inflation rate", importance="2")

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar/indicator/inflation%20rate?importance=2
        self.assertIn("/calendar/indicator/", called_url)
        self.assertIn(
            "?importance=2",
            called_url,
            f"Expected '?importance=2' after category path, got: {called_url}",
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_date_range_with_importance_combines_correctly(self, mock_request):
        """Test that date range + importance uses correct format"""
        mock_request.return_value = []

        te.getCalendarData(initDate="2016-01-01", endDate="2016-01-03", importance="3")

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar/country/all/2016-01-01/2016-01-03?importance=3
        self.assertIn("/calendar/country/all/", called_url)
        self.assertIn("2016-01-01", called_url)
        self.assertIn("2016-01-03", called_url)
        self.assertIn(
            "?importance=3",
            called_url,
            f"Expected '?importance=3' after dates, got: {called_url}",
        )

    @patch("tradingeconomics.functions.dataRequest")
    def test_no_query_params_has_no_question_mark(self, mock_request):
        """Test that URLs without query params don't have ? or &"""
        mock_request.return_value = []

        te.getCalendarData(country="united states")

        called_url = mock_request.call_args[1]["api_request"]

        # Should be /calendar/country/united%20states (no ? or &)
        self.assertNotIn(
            "?",
            called_url,
            f"Should not have '?' when no query params, got: {called_url}",
        )
        self.assertNotIn(
            "&",
            called_url,
            f"Should not have '&' when no query params, got: {called_url}",
        )


if __name__ == "__main__":
    unittest.main()
