import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits, LoginError
from tradingeconomics import glob


class TestGetStockSplitsErrors(unittest.TestCase):

    def test_get_stock_splits_no_credentials(self):
        # Test that AttributeError is raised when no API key is set
        original_apikey = glob.apikey
        try:
            delattr(glob, "apikey")
            with self.assertRaises(LoginError) as context:
                getStockSplits()

            self.assertIn("login", str(context.exception).lower())
        finally:
            glob.apikey = original_apikey


if __name__ == "__main__":
    unittest.main()
