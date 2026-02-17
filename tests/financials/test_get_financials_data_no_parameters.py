import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsData
from tradingeconomics import glob


class TestGetFinancialsDataNoParameters(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest", return_value={"companies": "ok"}
    )
    def test_financials_no_parameters(self, mock_request):
        # Get all companies when no parameters provided
        result = getFinancialsData()

        expected_url = "/financials/companies"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"companies": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"company": "Apple"}],
    )
    def test_financials_no_parameters_output_type_df(self, mock_request):
        result = getFinancialsData(output_type="df")

        expected_url = "/financials/companies"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"company": "Apple"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"company": "Microsoft"}],
    )
    def test_financials_no_parameters_output_type_raw(self, mock_request):
        result = getFinancialsData(output_type="raw")

        expected_url = "/financials/companies"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"company": "Microsoft"}])
