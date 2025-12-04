import unittest
from unittest.mock import patch
from tradingeconomics.news import getArticles
from tradingeconomics import glob


class TestGetArticlesBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"articles": "all"})
    def test_get_articles_no_parameters(self, mock_request):
        # Get all articles
        result = getArticles()

        expected_url = "https://api.tradingeconomics.com/articles/"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"articles": "country"})
    def test_get_articles_by_country(self, mock_request):
        # Get articles by country
        result = getArticles(country="United States")

        expected_url = "https://api.tradingeconomics.com/articles/country/United%20States"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest", return_value={"articles": "countries"}
    )
    def test_get_articles_by_multiple_countries(self, mock_request):
        # Get articles by multiple countries
        result = getArticles(country=["United States", "Portugal"])

        expected_url = "https://api.tradingeconomics.com/articles/country/United%20States,Portugal"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest", return_value={"articles": "indicator"}
    )
    def test_get_articles_by_indicator(self, mock_request):
        # Get articles by indicator
        result = getArticles(indicator="inflation rate")

        expected_url = "https://api.tradingeconomics.com/articles/indicator//inflation%20rate"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "indicator"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"articles": "country_indicator"},
    )
    def test_get_articles_by_country_and_indicator(self, mock_request):
        # Get articles by country and indicator
        result = getArticles(
            country=["United States", "Portugal"],
            indicator=["Imports", "Interest rate"],
        )

        expected_url = "https://api.tradingeconomics.com/articles/country/United%20States,Portugal/Imports,Interest%20rate"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "country_indicator"})
