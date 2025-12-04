import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsData
from tradingeconomics import glob


class TestGetFinancialsDataCountry(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.stringOrList", return_value="united%20states"
    )
    @patch("tradingeconomics.financials.fn.dataRequest", return_value={"country": "ok"})
    def test_financials_country_single(self, mock_request, mock_string_or_list):
        # Get financials data for single country
        result = getFinancialsData(country="united states")

        expected_url = "https://api.tradingeconomics.com/financials/companies?country=united%20states&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.stringOrList",
        return_value="united%20states%2Cchina",
    )
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value={"country": "multiple"},
    )
    def test_financials_country_multiple(self, mock_request, mock_string_or_list):
        # Get financials data for multiple countries
        result = getFinancialsData(country=["united states", "china"])

        expected_url = "https://api.tradingeconomics.com/financials/companies?country=united%20states%2Cchina&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"country": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.stringOrList", return_value="united%20states"
    )
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"country": "United States"}],
    )
    def test_financials_country_with_output_type(
        self, mock_request, mock_string_or_list
    ):
        # Test with output_type parameter
        result = getFinancialsData(country="united states", output_type="df")

        expected_url = "https://api.tradingeconomics.com/financials/companies?country=united%20states&c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"country": "United States"}])
