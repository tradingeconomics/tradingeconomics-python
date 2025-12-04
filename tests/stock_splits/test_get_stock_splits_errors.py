import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits, LoginError
from tradingeconomics import glob


class TestGetStockSplitsErrors(unittest.TestCase):

    @patch("tradingeconomics.stock_splits.glob.apikey", "")
    def test_get_stock_splits_no_credentials(self):
        # Test that HTTPError is raised when no API key is set (API returns 401)
        from urllib.error import HTTPError

        with self.assertRaises(HTTPError):
            getStockSplits()


if __name__ == "__main__":
    unittest.main()
