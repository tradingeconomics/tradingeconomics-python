import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsTicker(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "ticker"})
    def test_get_news_by_ticker(self, mock_request):
        # Get news by ticker
        result = getNews(ticker="AAPL:US")

        expected_url = "https://api.tradingeconomics.com/news/ticker/AAPL:US?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "ticker"})
