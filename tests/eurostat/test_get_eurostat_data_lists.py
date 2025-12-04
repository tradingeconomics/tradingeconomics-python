import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataLists(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"lists": "categories"}
    )
    def test_lists_parameter_categories(self, mock_request):
        # Request categories list
        result = getEurostatData(lists="categories")

        expected_url = "https://api.tradingeconomics.com/eurostat/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"lists": "categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"lists": "countries"}
    )
    def test_lists_parameter_countries(self, mock_request):
        # Request countries list
        result = getEurostatData(lists="countries")

        expected_url = "https://api.tradingeconomics.com/eurostat/countries"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"lists": "countries"})
