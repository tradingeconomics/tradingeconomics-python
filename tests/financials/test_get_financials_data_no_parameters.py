import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsData
from tradingeconomics import glob


class TestGetFinancialsDataNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest", return_value={"all": "companies"}
    )
    def test_financials_no_parameters(self, mock_request):
        # Get all companies when no parameters provided
        result = getFinancialsData()

        expected_url = "https://api.tradingeconomics.com/financials/companies?c=TESTKEY"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"all": "companies"})
