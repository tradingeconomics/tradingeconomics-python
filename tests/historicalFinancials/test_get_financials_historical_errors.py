import unittest
from unittest.mock import patch
from tradingeconomics.historicalFinancials import getFinancialsHistorical
from tradingeconomics import glob


class TestGetFinancialsHistoricalErrors(unittest.TestCase):

    def test_financials_historical_no_symbol(self):
        # Test that error message is returned when symbol is missing
        result = getFinancialsHistorical(category="assets")

        self.assertEqual(result, "symbol and category arguments are required")

    def test_financials_historical_no_category(self):
        # Test that error message is returned when category is missing
        result = getFinancialsHistorical(symbol="aapl:us")

        self.assertEqual(result, "symbol and category arguments are required")

    def test_financials_historical_no_parameters(self):
        # Test that error message is returned when both parameters are missing
        result = getFinancialsHistorical()

        self.assertEqual(result, "symbol and category arguments are required")
