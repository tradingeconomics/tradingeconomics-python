import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsDataByCategory
from tradingeconomics import glob


class TestGetFinancialsDataByCategory(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest", return_value={"category": "ok"}
    )
    def test_financials_by_category_single(self, mock_request):
        # Get financials data by single category
        result = getFinancialsDataByCategory(category="assets")

        expected_url = (
            "https://api.tradingeconomics.com/financials/category/assets"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"category": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"category": "Assets"}],
    )
    def test_financials_by_category_with_output_type(self, mock_request):
        # Test with output_type parameter
        result = getFinancialsDataByCategory(category="assets", output_type="df")

        expected_url = (
            "https://api.tradingeconomics.com/financials/category/assets"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"category": "Assets"}])
