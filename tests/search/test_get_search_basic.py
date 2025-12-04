import unittest
from unittest.mock import patch
from tradingeconomics.search import getSearch
from tradingeconomics import glob


class TestGetSearchBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "all_categories"},
    )
    def test_get_search_no_parameters(self, mock_request):
        # Get all search categories
        result = getSearch()

        expected_url = "https://api.tradingeconomics.com/search/categories?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "all_categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest", return_value={"search": "dict_output"}
    )
    def test_get_search_output_type_dict(self, mock_request):
        # Get search with dict output type
        result = getSearch(term="gold", output_type="dict")

        expected_url = "https://api.tradingeconomics.com/search/gold?c=TESTKEY"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="dict"
        )
        self.assertEqual(result, {"search": "dict_output"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.search.fn.dataRequest", return_value="df_output")
    def test_get_search_output_type_df(self, mock_request):
        # Get search with DataFrame output type
        result = getSearch(term="japan", output_type="df")

        expected_url = "https://api.tradingeconomics.com/search/japan?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, "df_output")

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.search.fn.dataRequest", return_value="raw_output")
    def test_get_search_output_type_raw(self, mock_request):
        # Get search with raw output type
        result = getSearch(term="inflation", output_type="raw")

        expected_url = "https://api.tradingeconomics.com/search/inflation?c=TESTKEY"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, "raw_output")


if __name__ == "__main__":
    unittest.main()
