import unittest
from unittest.mock import patch
from tradingeconomics.worldBank import (
    getWBCategories,
    getWBCountry,
    LoginError,
    WebRequestError,
)
from tradingeconomics import glob


class TestGetWBCategoriesErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        side_effect=WebRequestError("Request failed: HTTP Error 401: Unauthorized"),
    )
    def test_get_wb_categories_no_credentials(self, mock_request):
        # Test that WebRequestError is raised when no API key is set (API returns 401)
        with self.assertRaises(WebRequestError):
            getWBCategories()


class TestGetWBCountryErrors(unittest.TestCase):

    @patch.object(glob, "apikey", "")
    @patch(
        "tradingeconomics.worldBank.fn.dataRequest",
        side_effect=WebRequestError("Request failed: HTTP Error 401: Unauthorized"),
    )
    def test_get_wb_country_no_credentials(self, mock_request):
        # Test that WebRequestError is raised when no API key is set (API returns 401)
        with self.assertRaises(WebRequestError):
            getWBCountry(country="portugal")


if __name__ == "__main__":
    unittest.main()
