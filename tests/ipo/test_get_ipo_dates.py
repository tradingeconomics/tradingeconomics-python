import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "start_date"})
    def test_get_ipo_with_start_date(self, mock_request, mock_validate):
        # Get IPO data with start date
        result = getIpo(startDate="2023-10-01")

        expected_url = "https://api.tradingeconomics.com/ipo?c=TESTKEY&d1=2023-10-01"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "start_date"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.ipo.fn.validatePeriod")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "date_range"})
    def test_get_ipo_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get IPO data with date range
        result = getIpo(startDate="2023-10-01", endDate="2023-10-31")

        expected_url = (
            "https://api.tradingeconomics.com/ipo?c=TESTKEY&d1=2023-10-01&d2=2023-10-31"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "date_range"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.ipo.fn.validatePeriod")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "ticker_dates"})
    def test_get_ipo_ticker_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get IPO data for ticker with date range
        result = getIpo(ticker="SWIN", startDate="2023-10-01", endDate="2023-10-31")

        expected_url = "https://api.tradingeconomics.com/ipo/ticker/SWIN?c=TESTKEY&d1=2023-10-01&d2=2023-10-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "ticker_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.ipo.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.ipo.fn.dataRequest", return_value={"ipo": "country_date"})
    def test_get_ipo_country_with_start_date(self, mock_request, mock_validate):
        # Get IPO data for countries with start date
        result = getIpo(country=["United States", "Hong Kong"], startDate="2023-10-31")

        expected_url = "https://api.tradingeconomics.com/ipo/country/United%20States,Hong%20Kong?c=TESTKEY&d1=2023-10-31"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ipo": "country_date"})
