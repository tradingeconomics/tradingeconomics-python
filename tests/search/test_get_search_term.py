import unittest
from unittest.mock import patch
from tradingeconomics.search import getSearch
from tradingeconomics import glob


class TestGetSearchTerm(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest", return_value={"search": "single_term"}
    )
    def test_get_search_single_term(self, mock_request):
        # Get search by single term
        result = getSearch(term="gold")

        expected_url = "https://api.tradingeconomics.com/search/gold?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "single_term"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "multiple_terms"},
    )
    def test_get_search_multiple_terms(self, mock_request):
        # Get search by multiple terms
        result = getSearch(term=["gold", "silver"])

        expected_url = "https://api.tradingeconomics.com/search/gold,silver?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "multiple_terms"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.search.fn.dataRequest",
        return_value={"search": "term_with_spaces"},
    )
    def test_get_search_term_with_spaces(self, mock_request):
        # Get search by term with spaces
        result = getSearch(term="united states")

        expected_url = (
            "https://api.tradingeconomics.com/search/united%20states?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"search": "term_with_spaces"})


if __name__ == "__main__":
    unittest.main()
