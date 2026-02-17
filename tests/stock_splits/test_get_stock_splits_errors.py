import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits, LoginError, WebRequestError
from tradingeconomics import glob


class TestGetStockSplitsErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        side_effect=WebRequestError("Request failed: HTTP Error 401: Unauthorized"),
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_no_credentials(self, mock_check_dates, mock_request):
        # Test that WebRequestError is raised when no API key is set (API returns 401)
        with self.assertRaises(WebRequestError):
            getStockSplits()


if __name__ == "__main__":
    unittest.main()
