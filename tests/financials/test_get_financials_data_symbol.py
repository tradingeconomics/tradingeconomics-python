import unittest
from unittest.mock import patch
from tradingeconomics.financials import getFinancialsData
from tradingeconomics import glob


class TestGetFinancialsDataSymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.financials.fn.stringOrList", return_value="aapl:us")
    @patch("tradingeconomics.financials.fn.dataRequest", return_value={"symbol": "ok"})
    def test_financials_symbol_single(self, mock_request, mock_string_or_list):
        # Get financials data for single symbol
        result = getFinancialsData(symbol="aapl:us")

        expected_url = "https://api.tradingeconomics.com/financials/symbol/aapl:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.financials.fn.stringOrList", return_value="aapl:us%2Cmsft:us"
    )
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value={"symbol": "multiple"},
    )
    def test_financials_symbol_multiple(self, mock_request, mock_string_or_list):
        # Get financials data for multiple symbols
        result = getFinancialsData(symbol=["aapl:us", "msft:us"])

        expected_url = (
            "https://api.tradingeconomics.com/financials/symbol/aapl:us%2Cmsft:us"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "multiple"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.financials.fn.stringOrList", return_value="aapl:us")
    @patch(
        "tradingeconomics.financials.fn.dataRequest",
        return_value=[{"symbol": "AAPL:US"}],
    )
    def test_financials_symbol_with_output_type(
        self, mock_request, mock_string_or_list
    ):
        # Test with output_type parameter
        result = getFinancialsData(symbol="aapl:us", output_type="df")

        expected_url = "https://api.tradingeconomics.com/financials/symbol/aapl:us"

        mock_request.assert_called_once_with(api_request=expected_url, output_type="df")
        self.assertEqual(result, [{"symbol": "AAPL:US"}])
