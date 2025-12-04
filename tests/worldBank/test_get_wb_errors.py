import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBCategories, getWBCountry, LoginError
from tradingeconomics import glob


class TestGetWBCategoriesErrors(unittest.TestCase):

    @patch("tradingeconomics.worldBank.glob.apikey", "")
    def test_get_wb_categories_no_credentials(self):
        # Test that HTTPError is raised when no API key is set (API returns 401)
        from urllib.error import HTTPError

        with self.assertRaises(HTTPError):
            getWBCategories()


class TestGetWBCountryErrors(unittest.TestCase):

    @patch("tradingeconomics.worldBank.glob.apikey", "")
    def test_get_wb_country_no_credentials(self):
        # Test that HTTPError is raised when no API key is set (API returns 401)
        from urllib.error import HTTPError

        with self.assertRaises(HTTPError):
            getWBCountry(country="portugal")


if __name__ == "__main__":
    unittest.main()
