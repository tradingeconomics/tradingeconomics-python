import unittest
from unittest.mock import patch
from tradingeconomics.historicalEurostat import getHistoricalEurostat
from tradingeconomics import glob


class TestGetHistoricalEurostatErrors(unittest.TestCase):

    def test_historical_eurostat_no_id_error(self):
        # Test that ValueError is raised when ID is None
        with self.assertRaises(ValueError) as context:
            getHistoricalEurostat(ID=None)

        self.assertEqual(str(context.exception), "An ID needs to be supplied.")

    def test_historical_eurostat_no_id_parameter(self):
        # Test that ValueError is raised when ID is not provided
        with self.assertRaises(ValueError) as context:
            getHistoricalEurostat()

        self.assertEqual(str(context.exception), "An ID needs to be supplied.")
