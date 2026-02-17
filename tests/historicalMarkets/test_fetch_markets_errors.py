import unittest
from unittest.mock import patch
from tradingeconomics.historicalMarkets import fetchMarkets
from tradingeconomics.historicalMarkets import DateError
from tradingeconomics import glob


class TestFetchMarketsErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.historicalMarkets.fn.validate",
        side_effect=ValueError("Invalid date"),
    )
    def test_fetch_markets_invalid_init_date(self, mock_validate):
        # Test that DateError is raised when initDate format is invalid
        with self.assertRaises(DateError) as context:
            fetchMarkets(symbol="indu:ind", initDate="invalid-date")

        self.assertIn("Incorrect initDate format", str(context.exception))

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalMarkets.fn.validate")
    def test_fetch_markets_invalid_end_date(self, mock_validate):
        # Test that DateError is raised when endDate format is invalid
        # First call for initDate succeeds, second call for endDate fails
        mock_validate.side_effect = ["%Y-%m-%d", ValueError("Invalid date")]

        with self.assertRaises(DateError) as context:
            fetchMarkets(
                symbol="indu:ind", initDate="2017-01-01", endDate="invalid-date"
            )

        self.assertIn("Incorrect endDate format", str(context.exception))

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.historicalMarkets.fn.validate", return_value="%Y-%m-%d")
    @patch(
        "tradingeconomics.historicalMarkets.fn.validatePeriod",
        side_effect=ValueError("Invalid period"),
    )
    def test_fetch_markets_invalid_period(self, mock_validate_period, mock_validate):
        # Test that DateError is raised when period is invalid
        with self.assertRaises(DateError) as context:
            fetchMarkets(symbol="indu:ind", initDate="2017-06-15", endDate="2017-01-01")

        self.assertIn("Invalid time period", str(context.exception))
