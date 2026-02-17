import unittest
from unittest.mock import patch
from tradingeconomics.news import getNews
from tradingeconomics import glob


class TestGetNewsErrors(unittest.TestCase):

    def test_get_news_start_with_start_date_error(self):
        # Test error when both start and start_date are provided
        result = getNews(start="10", start_date="2021-02-02")

        self.assertEqual(
            result,
            'Please, enter the pair "start" and "limit" or the pair "start_date" and "end_date"',
        )
