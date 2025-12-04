import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits
from tradingeconomics import glob


class TestGetStockSplitsTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "single_ticker"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_single_ticker(self, mock_check_dates, mock_request):
        # Get stock splits by single ticker
        result = getStockSplits(ticker="AAPL:US")

        expected_url = "/splits/ticker/AAPL:US"

        mock_check_dates.assert_called_once_with(
            "/splits/ticker/AAPL:US",
            None,
            None,
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "single_ticker"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "multiple_tickers"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_multiple_tickers(self, mock_check_dates, mock_request):
        # Get stock splits by multiple tickers
        result = getStockSplits(ticker=["AAPL:US", "MSFT:US"])

        expected_url = "/splits/ticker/AAPL:US,MSFT:US"

        mock_check_dates.assert_called_once_with(
            "/splits/ticker/AAPL:US,MSFT:US",
            None,
            None,
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "multiple_tickers"})


if __name__ == "__main__":
    unittest.main()
