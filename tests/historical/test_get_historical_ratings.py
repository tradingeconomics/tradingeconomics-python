import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalRatings
from tradingeconomics import glob


class TestGetHistoricalRatings(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"ratings": "ok"})
    def test_historical_ratings_country_single(self, mock_request):
        # Get historical ratings for single country
        result = getHistoricalRatings(country="United States")

        expected_url = "/ratings/historical/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ratings": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"ratings": "multiple"},
    )
    def test_historical_ratings_country_multiple(self, mock_request):
        # Get historical ratings for multiple countries
        result = getHistoricalRatings(country=["United States", "United Kingdom"])

        expected_url = "/ratings/historical/united%20states%2Cunited%20kingdom"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ratings": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"ratings": "with_date"},
    )
    def test_historical_ratings_with_init_date(self, mock_request):
        # Get historical ratings with init date
        result = getHistoricalRatings(country="United States", initDate="2011-01-01")

        expected_url = "/ratings/historical/united%20states/2011-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ratings": "with_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"ratings": "with_dates"},
    )
    def test_historical_ratings_with_date_range(self, mock_request):
        # Get historical ratings with date range
        result = getHistoricalRatings(
            country="United States", initDate="2011-01-01", endDate="2012-01-01"
        )

        expected_url = "/ratings/historical/united%20states/2011-01-01/2012-01-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ratings": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest", return_value=[{"rating": "AAA"}]
    )
    def test_historical_ratings_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getHistoricalRatings(country="United States", output_type="df")

        expected_url = "/ratings/historical/united%20states"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"rating": "AAA"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"raw": "json", "rating": "AAA"},
    )
    def test_historical_ratings_output_type_raw(self, mock_request):
        # Test with output_type='raw' parameter
        result = getHistoricalRatings(country="United States", output_type="raw")

        expected_url = "/ratings/historical/united%20states"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"raw": "json", "rating": "AAA"})
