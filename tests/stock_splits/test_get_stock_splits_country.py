import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits
from tradingeconomics import glob


class TestGetStockSplitsCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "single_country"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_single_country(self, mock_check_dates, mock_request):
        # Get stock splits by single country
        result = getStockSplits(country="United States")

        expected_url = "/splits/country/United%20States"

        mock_check_dates.assert_called_once_with(
            "/splits/country/United%20States",
            None,
            None,
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "single_country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "multiple_countries"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_multiple_countries(self, mock_check_dates, mock_request):
        # Get stock splits by multiple countries
        result = getStockSplits(country=["United States", "Canada"])

        expected_url = "/splits/country/United%20States,Canada"

        mock_check_dates.assert_called_once_with(
            "/splits/country/United%20States,Canada",
            None,
            None,
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "multiple_countries"})


if __name__ == "__main__":
    unittest.main()
