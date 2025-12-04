import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsBasic(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "all"})
    def test_get_news_no_parameters(self, mock_request):
        # Get all news
        result = getNews()

        expected_url = "https://api.tradingeconomics.com/news"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "all"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "df"})
    def test_get_news_with_output_type(self, mock_request):
        # Get news with output type
        result = getNews(output_type="df")

        expected_url = "https://api.tradingeconomics.com/news"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"news": "df"})
