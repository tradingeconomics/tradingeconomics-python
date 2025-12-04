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

        expected_url = "/eurostat/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"lists": "categories"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"lists": "countries"}
    )
    def test_lists_parameter_countries(self, mock_request):
        # Request countries list
        result = getEurostatData(lists="countries")

        expected_url = "/eurostat/countries"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"lists": "countries"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"lists": "df"})
    def test_lists_categories_output_type_df(self, mock_request):
        result = getEurostatData(lists="categories", output_type="df")

        expected_url = "/eurostat/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, {"lists": "df"})
