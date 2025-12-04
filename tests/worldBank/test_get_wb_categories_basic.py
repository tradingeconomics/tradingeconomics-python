import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBCategories
from tradingeconomics import glob


class TestGetWBCategoriesBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest", return_value={"categories": "all"}
    )
    def test_get_wb_categories_no_parameters(self, mock_request):
        # Get all World Bank categories
        result = getWBCategories()

        expected_url = "https://api.tradingeconomics.com/worldBank/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        return_value={"categories": "dict_output"},
    )
    def test_get_wb_categories_output_type_dict(self, mock_request):
        # Get categories with dict output type
        result = getWBCategories(output_type="dict")

        expected_url = "https://api.tradingeconomics.com/worldBank/categories"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="dict"
        )
        self.assertEqual(result, {"categories": "dict_output"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.worldBank.fn.dataRequest", return_value="df_output")
    def test_get_wb_categories_output_type_df(self, mock_request):
        # Get categories with DataFrame output type
        result = getWBCategories(output_type="df")

        expected_url = "https://api.tradingeconomics.com/worldBank/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "df_output")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.worldBank.fn.dataRequest", return_value="raw_output")
    def test_get_wb_categories_output_type_raw(self, mock_request):
        # Get categories with raw output type
        result = getWBCategories(output_type="raw")

        expected_url = "https://api.tradingeconomics.com/worldBank/categories"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, "raw_output")


if __name__ == "__main__":
    unittest.main()
