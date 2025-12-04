import unittest
from unittest.mock import patch
from tradingeconomics.search import getSearch
from tradingeconomics import glob


class TestGetSearchTermAndCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "term_single_category"},
    )
    def test_get_search_term_and_single_category(self, mock_request):
        # Get search by term and single category
        result = getSearch(term="japan", category="markets")

        expected_url = "/search/japan?category=markets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "term_single_category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "term_multiple_categories"},
    )
    def test_get_search_term_and_multiple_categories(self, mock_request):
        # Get search by term and multiple categories
        result = getSearch(term="gold", category=["markets", "indicators"])

        expected_url = "/search/gold?category=markets,indicators"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "term_multiple_categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "multiple_terms_category"},
    )
    def test_get_search_multiple_terms_and_category(self, mock_request):
        # Get search by multiple terms and category
        result = getSearch(term=["japan", "china"], category="indicators")

        expected_url = "/search/japan,china?category=indicators"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "multiple_terms_category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "term_spaces_category"},
    )
    def test_get_search_term_with_spaces_and_category(self, mock_request):
        # Get search by term with spaces and category
        result = getSearch(term="united states", category="markets")

        expected_url = "/search/united%20states?category=markets"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "term_spaces_category"})


if __name__ == "__main__":
    unittest.main()
