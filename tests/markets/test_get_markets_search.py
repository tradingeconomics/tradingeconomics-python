import unittest
from unittest.mock import patch
from tradingeconomics.markets import getMarketsSearch
from tradingeconomics import glob


class TestGetMarketsSearch(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"search": "country"}
    )
    def test_get_markets_search_by_country(self, mock_request):
        # Search markets by country
        result = getMarketsSearch(country="japan")

        expected_url = "/markets/search/japan"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"search": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"search": "category"}
    )
    def test_get_markets_search_by_country_and_category(self, mock_request):
        # Search markets by country and category
        result = getMarketsSearch(country="japan", category="index")

        expected_url = "/markets/search/japan?category=index"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"search": "category"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"search": "categories"}
    )
    def test_get_markets_search_multiple_categories(self, mock_request):
        # Search markets by country and multiple categories
        result = getMarketsSearch(country="japan", category=["index", "markets"])

        expected_url = "/markets/search/japan?category=index%2Cmarkets"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"search": "categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.markets.fn.dataRequest", return_value={"search": "page"})
    def test_get_markets_search_with_page(self, mock_request):
        # Search markets with page parameter
        result = getMarketsSearch(country="japan", category="index", page=2)

        expected_url = "/markets/search/japan?category=index&page=2"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"search": "page"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest", return_value={"search": "countries"}
    )
    def test_get_markets_search_multiple_countries(self, mock_request):
        # Search markets by multiple countries
        result = getMarketsSearch(country=["japan", "china"])

        expected_url = "/markets/search/japan%2Cchina"

        mock_request.assert_called_once_with(expected_url, None)
        self.assertEqual(result, {"search": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.markets.fn.dataRequest",
        return_value={"raw": "json", "search": "data"},
    )
    def test_get_markets_search_with_output_type_raw(self, mock_request):
        # Test with output_type='raw'
        result = getMarketsSearch(country="japan", category="index", output_type="raw")

        expected_url = "/markets/search/japan?category=index"

        mock_request.assert_called_once_with(expected_url, "raw")
        self.assertEqual(result, {"raw": "json", "search": "data"})
