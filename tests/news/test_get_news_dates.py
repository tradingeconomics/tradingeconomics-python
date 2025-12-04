import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "dates"})
    def test_get_news_with_date_range(self, mock_request):
        # Get news with date range
        result = getNews(start_date="2021-02-02", end_date="2021-03-03")

        expected_url = "https://api.tradingeconomics.com/news?c=TESTKEY&d1=2021-02-02&d2=2021-03-03"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest", return_value={"news": "indicator_dates"}
    )
    def test_get_news_indicator_with_dates(self, mock_request):
        # Get news by indicator with date range
        result = getNews(
            indicator="inflation rate", start_date="2021-02-02", end_date="2021-03-03"
        )

        expected_url = "https://api.tradingeconomics.com/news/indicator/inflation%20rate?c=TESTKEY&d1=2021-02-02&d2=2021-03-03"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "indicator_dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest", return_value={"news": "country_dates"}
    )
    def test_get_news_country_indicator_with_dates(self, mock_request):
        # Get news by country and indicator with date range
        result = getNews(
            country=["brazil", "canada"],
            indicator=["Housing Starts", "Stock Market"],
            start_date="2021-02-02",
            end_date="2021-03-03",
        )

        expected_url = "https://api.tradingeconomics.com/news/country/brazil,canada/Housing%20Starts,Stock%20Market?c=TESTKEY&d1=2021-02-02&d2=2021-03-03"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "country_dates"})
