import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits
from tradingeconomics import glob


class TestGetStockSplitsDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "with_dates"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: (
            url + "?d1=2023-01-01&d2=2023-12-31" if d1 else url
        ),
    )
    def test_get_stock_splits_with_date_range(self, mock_check_dates, mock_request):
        # Get stock splits with date range
        result = getStockSplits(startDate="2023-01-01", endDate="2023-12-31")

        expected_url = "/splits?d1=2023-01-01&d2=2023-12-31"

        mock_check_dates.assert_called_once_with(
            "/splits",
            "2023-01-01",
            "2023-12-31",
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "with_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "ticker_dates"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: (
            url + "?d1=2023-01-01&d2=2023-12-31" if d1 else url
        ),
    )
    def test_get_stock_splits_ticker_with_dates(self, mock_check_dates, mock_request):
        # Get stock splits by ticker with date range
        result = getStockSplits(
            ticker="AAPL:US", startDate="2023-01-01", endDate="2023-12-31"
        )

        expected_url = "/splits/ticker/AAPL:US?d1=2023-01-01&d2=2023-12-31"

        mock_check_dates.assert_called_once_with(
            "/splits/ticker/AAPL:US",
            "2023-01-01",
            "2023-12-31",
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "ticker_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "country_dates"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: (
            url + "?d1=2023-01-01&d2=2023-12-31" if d1 else url
        ),
    )
    def test_get_stock_splits_country_with_dates(self, mock_check_dates, mock_request):
        # Get stock splits by country with date range
        result = getStockSplits(
            country="United States", startDate="2023-01-01", endDate="2023-12-31"
        )

        expected_url = "/splits/country/United%20States?d1=2023-01-01&d2=2023-12-31"

        mock_check_dates.assert_called_once_with(
            "/splits/country/United%20States",
            "2023-01-01",
            "2023-12-31",
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "country_dates"})


if __name__ == "__main__":
    unittest.main()
