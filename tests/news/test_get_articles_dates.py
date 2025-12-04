import unittest
from unittest.mock import patch
from tradingeconomics.news import getArticles
from tradingeconomics import glob


class TestGetArticlesDates(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.news.fn.validatePeriod")
    @patch("tradingeconomics.news.fn.dataRequest", return_value={"articles": "dates"})
    def test_get_articles_with_date_range(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get articles with date range
        result = getArticles(
            country="United States", initDate="2015-10-10", endDate="2017-10-10"
        )

        expected_url = "/articles/country/United%20States/from/2015-10-10/2017-10-10"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "dates"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.news.fn.validate", return_value="%Y-%m-%d")
    @patch("tradingeconomics.news.fn.validatePeriod")
    @patch(
        "tradingeconomics.news.fn.dataRequest",
        return_value={"articles": "countries_dates"},
    )
    def test_get_articles_multiple_countries_with_dates(
        self, mock_request, mock_validate_period, mock_validate
    ):
        # Get articles by multiple countries with date range
        result = getArticles(
            country=["United States", "Portugal"],
            initDate="2015-10-10",
            endDate="2017-10-10",
        )

        expected_url = (
            "/articles/country/United%20States,Portugal/from/2015-10-10/2017-10-10"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"articles": "countries_dates"})
