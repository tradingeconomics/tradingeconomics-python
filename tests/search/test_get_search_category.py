import unittest
from unittest.mock import patch
from tradingeconomics.search import getSearch
from tradingeconomics import glob


class TestGetSearchCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "single_category"},
    )
    def test_get_search_single_category(self, mock_request):
        # Get search by single category
        result = getSearch(category="markets")

        expected_url = "/search/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "single_category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "multiple_categories"},
    )
    def test_get_search_multiple_categories(self, mock_request):
        # Get search by multiple categories
        result = getSearch(category=["markets", "indicators"])

        expected_url = "/search/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "multiple_categories"})


if __name__ == "__main__":
    unittest.main()
