import unittest
from unittest.mock import patch
from tradingeconomics.stock_splits import getStockSplits
from tradingeconomics import glob


class TestGetStockSplitsBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest", return_value={"splits": "all"}
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_no_parameters(self, mock_check_dates, mock_request):
        # Get all stock splits
        result = getStockSplits()

        expected_url = "https://api.tradingeconomics.com/splits?c=TESTKEY"

        mock_check_dates.assert_called_once_with(
            "https://api.tradingeconomics.com/splits?c=TESTKEY", None, None
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"splits": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.stock_splits.fn.dataRequest",
        return_value={"splits": "dict_output"},
    )
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_output_type_dict(self, mock_check_dates, mock_request):
        # Get stock splits with dict output type
        result = getStockSplits(output_type="dict")

        expected_url = "https://api.tradingeconomics.com/splits?c=TESTKEY"

        mock_check_dates.assert_called_once_with(
            "https://api.tradingeconomics.com/splits?c=TESTKEY", None, None
        )
        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="dict"
        )
        self.assertEqual(result, {"splits": "dict_output"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.stock_splits.fn.dataRequest", return_value="df_output")
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_output_type_df(self, mock_check_dates, mock_request):
        # Get stock splits with DataFrame output type
        result = getStockSplits(output_type="df")

        expected_url = "https://api.tradingeconomics.com/splits?c=TESTKEY"

        mock_check_dates.assert_called_once_with(
            "https://api.tradingeconomics.com/splits?c=TESTKEY", None, None
        )
        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "df_output")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.stock_splits.fn.dataRequest", return_value="raw_output")
    @patch(
        "tradingeconomics.stock_splits.fn.checkDates",
        side_effect=lambda url, d1, d2: url,
    )
    def test_get_stock_splits_output_type_raw(self, mock_check_dates, mock_request):
        # Get stock splits with raw output type
        result = getStockSplits(output_type="raw")

        expected_url = "https://api.tradingeconomics.com/splits?c=TESTKEY"

        mock_check_dates.assert_called_once_with(
            "https://api.tradingeconomics.com/splits?c=TESTKEY", None, None
        )
        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, "raw_output")


if __name__ == "__main__":
    unittest.main()
