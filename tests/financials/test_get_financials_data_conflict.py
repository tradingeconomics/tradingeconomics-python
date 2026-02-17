import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsData
from tradingeconomics import glob


class TestGetFinancialsDataConflict(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    def test_financials_country_and_symbol_conflict(self):
        # When both country and symbol are provided, should return error message
        result = getFinancialsData(country="united states", symbol="aapl:us")

        self.assertEqual(
            result, "Cannot pass country and symbol arguments at the same time."
        )
