import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "country"})
    def test_get_news_by_country(self, mock_request):
        # Get news by country
        result = getNews(country="brazil")

        expected_url = "https://api.tradingeconomics.com/news/country/brazil?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "country"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "countries"})
    def test_get_news_by_multiple_countries(self, mock_request):
        # Get news by multiple countries
        result = getNews(country=["brazil", "canada"])

        expected_url = (
            "https://api.tradingeconomics.com/news/country/brazil,canada?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "countries"})
