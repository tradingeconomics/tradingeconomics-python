import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsPagination(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "start_limit"})
    def test_get_news_with_start_and_limit(self, mock_request):
        # Get news with start and limit
        result = getNews(start="15", limit="15")

        expected_url = (
            "https://api.tradingeconomics.com/news?c=TESTKEY&limit=15&start=15"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "start_limit"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"news": "country_start_limit"},
    )
    def test_get_news_country_with_start_and_limit(self, mock_request):
        # Get news by country with start and limit
        result = getNews(
            country="United States",
            indicator="Imports",
            start="10",
            limit="20",
            output_type="df",
        )

        expected_url = "https://api.tradingeconomics.com/news/country/United%20States/Imports?c=TESTKEY&limit=20&start=10"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"news": "country_start_limit"})
