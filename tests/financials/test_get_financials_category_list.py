import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsCategoryList
from tradingeconomics import glob


class TestGetFinancialsCategoryList(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest", return_value={"categories": "ok"}
    )
    def test_get_financials_category_list(self, mock_request):
        # Get list of financial categories
        result = getFinancialsCategoryList()

        expected_url = "/financials/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"categories": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"category": "assets"}],
    )
    def test_get_financials_category_list_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getFinancialsCategoryList(output_type="df")

        expected_url = "/financials/categories"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"category": "assets"}])

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"category": "Debt"}],
    )
    def test_get_financials_category_list_output_type_raw(self, mock_request):
        result = getFinancialsCategoryList(output_type="raw")

        expected_url = "/financials/categories"

        mock_request.assert_called_once_with(
            api_request=expected_url, output_type="raw"
        )
        self.assertEqual(result, [{"category": "Debt"}])
