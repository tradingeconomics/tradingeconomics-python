import unittest
from unittest.mock import patch
from tradingeconomics.historical import getHistoricalLatest
from tradingeconomics import glob


class TestGetHistoricalLatest(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"latest": "ok"})
    def test_historical_latest_no_parameters(self, mock_request):
        # Get latest historical data with no parameters
        result = getHistoricalLatest()

        expected_url = "https://api.tradingeconomics.com/historical/latest"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"latest": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.stringOrList", return_value="Brazil")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"country": "ok"})
    def test_historical_latest_single_country(self, mock_request, mock_string_or_list):
        # Get latest historical data for single country
        result = getHistoricalLatest(country="Brazil")

        expected_url = (
            "https://api.tradingeconomics.com/historical/latest?country=Brazil"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.stringOrList",
        return_value="Brazil%2CUnited%20States",
    )
    @patch(
        "tradingeconomics.historical.fn.dataRequest",
        return_value={"country": "multiple"},
    )
    def test_historical_latest_multiple_countries(
        self, mock_request, mock_string_or_list
    ):
        # Get latest historical data for multiple countries
        result = getHistoricalLatest(country=["Brazil", "United States"])

        expected_url = "https://api.tradingeconomics.com/historical/latest?country=Brazil%2CUnited%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value={"date": "ok"})
    def test_historical_latest_with_date(self, mock_request):
        # Get latest historical data for specific date
        result = getHistoricalLatest(date="2025-08-26")

        expected_url = (
            "https://api.tradingeconomics.com/historical/latest?date=2025-08-26"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"date": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historical.fn.stringOrList",
        return_value="Brazil%2CUnited%20States",
    )
    @patch(
        "tradingeconomics.historical.fn.dataRequest", return_value={"combined": "ok"}
    )
    def test_historical_latest_country_and_date(
        self, mock_request, mock_string_or_list
    ):
        # Get latest historical data for countries and date
        result = getHistoricalLatest(
            country=["Brazil", "United States"], date="2025-08-26"
        )

        expected_url = "https://api.tradingeconomics.com/historical/latest?country=Brazil%2CUnited%20States&date=2025-08-26"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"combined": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historical.fn.dataRequest", return_value=[{"value": 100}])
    def test_historical_latest_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getHistoricalLatest(output_type="df")

        expected_url = "https://api.tradingeconomics.com/historical/latest"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"value": 100}])
