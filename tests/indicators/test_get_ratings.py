import unittest
from unittest.mock import patch
from tradingeconomics.indicators import getRatings
from tradingeconomics import glob


class TestGetRatings(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"ratings": "all"}
    )
    def test_get_ratings_no_parameters(self, mock_request):
        # Get all ratings
        result = getRatings()

        expected_url = "https://api.tradingeconomics.com/ratings"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ratings": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"ratings": "country"},
    )
    def test_get_ratings_by_country(self, mock_request):
        # Get ratings for specific country
        result = getRatings(country="United States")

        expected_url = (
            "https://api.tradingeconomics.com/ratings/united%20states"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ratings": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest",
        return_value={"ratings": "countries"},
    )
    def test_get_ratings_by_multiple_countries(self, mock_request):
        # Get ratings for multiple countries
        result = getRatings(country=["United States", "Portugal"])

        expected_url = "https://api.tradingeconomics.com/ratings/United%20States%2CPortugal"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"ratings": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.indicators.fn.dataRequest", return_value={"ratings": "raw"}
    )
    def test_get_ratings_with_output_type(self, mock_request):
        # Get ratings with custom output type
        result = getRatings(country="United States", output_type="raw")

        expected_url = (
            "https://api.tradingeconomics.com/ratings/united%20states"
        )

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, {"ratings": "raw"})
