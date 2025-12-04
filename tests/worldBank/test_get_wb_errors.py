import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import getWBCategories, getWBCountry, LoginError
from tradingeconomics import glob


class TestGetWBCategoriesErrors(unittest.TestCase):

    def test_get_wb_categories_no_credentials(self):
        # Test that LoginError is raised when no API key is set
        original_apikey = glob.apikey
        try:
            delattr(glob, "apikey")
            with self.assertRaises(LoginError) as context:
                getWBCategories()

            self.assertIn("login", str(context.exception).lower())
        finally:
            glob.apikey = original_apikey


class TestGetWBCountryErrors(unittest.TestCase):

    def test_get_wb_country_no_credentials(self):
        # Test that LoginError is raised when no API key is set
        original_apikey = glob.apikey
        try:
            delattr(glob, "apikey")
            with self.assertRaises(LoginError) as context:
                getWBCountry(country="portugal")

            self.assertIn("login", str(context.exception).lower())
        finally:
            glob.apikey = original_apikey


if __name__ == "__main__":
    unittest.main()
