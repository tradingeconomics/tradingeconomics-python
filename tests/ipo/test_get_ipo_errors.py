import unittest
from unittest.mock import patch
from tradingeconomics.ipo import getIpo
from tradingeconomics import glob


class TestGetIpoErrors(unittest.TestCase):

    def test_get_ipo_ticker_and_country_error(self):
        # Test that ValueError is raised when both ticker and country are provided
        with self.assertRaises(ValueError) as context:
            getIpo(ticker="SWIN", country="United States")

        self.assertEqual(
            str(context.exception), "ticker and country cannot be used together"
        )
