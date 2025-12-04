import unittest
from unittest.mock import patch
from tradingeconomics.news import getArticles
from tradingeconomics import glob


class TestGetArticlesPagination(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest", return_value={"articles": "pagination"}
    )
    def test_get_articles_with_start_and_limit(self, mock_request):
        # Get articles with start and limit
        result = getArticles(start=10, lim=20, output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/articles/?lim=20&start=10"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"articles": "pagination"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"articles": "country_pagination"},
    )
    def test_get_articles_country_with_start_and_limit(self, mock_request):
        # Get articles by country with start and limit
        result = getArticles(
            country="United States", indicator="inflation rate", start=20, lim=100
        )

        expected_url = "https://api.tradingeconomics.com/articles/country/United%20States/inflation%20rate?lim=100&start=20"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "country_pagination"})
