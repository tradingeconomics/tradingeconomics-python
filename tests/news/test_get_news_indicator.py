import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsIndicator(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "indicator"})
    def test_get_news_by_indicator(self, mock_request):
        # Get news by indicator
        result = getNews(indicator="inflation rate")

        expected_url = "/news/indicator/inflation%20rate"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "indicator"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"news": "indicators"})
    def test_get_news_by_multiple_indicators(self, mock_request):
        # Get news by multiple indicators
        result = getNews(indicator=["inflation rate", "gdp"])

        expected_url = "/news/indicator/inflation%20rate,gdp"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "indicators"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"news": "country_indicator"},
    )
    def test_get_news_by_country_and_indicator(self, mock_request):
        # Get news by country and indicator
        result = getNews(country="United States", indicator="Imports")

        expected_url = "/news/country/United%20States/Imports"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "country_indicator"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"news": "countries_indicators"},
    )
    def test_get_news_by_multiple_countries_and_indicators(self, mock_request):
        # Get news by multiple countries and indicators
        result = getNews(
            country=["brazil", "canada"], indicator=["Housing Starts", "Stock Market"]
        )

        expected_url = "/news/country/brazil,canada/Housing%20Starts,Stock%20Market"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"news": "countries_indicators"})
