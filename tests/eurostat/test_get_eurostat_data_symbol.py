import unittest
from unittest.mock import patch
from tradingeconomics.eurostat import getEurostatData
from tradingeconomics import glob


class TestGetEurostatDataSymbol(unittest.TestCase):

    @patch.object(glob, "apikey", "TESTKEY")
    @patch("tradingeconomics.eurostat.fn.dataRequest", return_value={"symbol": "ok"})
    def test_symbol_parameter_single(self, mock_request):
        # Provide a single symbol and ensure URL is built correctly
        result = getEurostatData(symbol="51640")

        expected_url = (
            "https://api.tradingeconomics.com/eurostat/symbol/51640?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "ok"})

    @patch.object(glob, "apikey", "TESTKEY")
    @patch(
        "tradingeconomics.eurostat.fn.dataRequest", return_value={"symbol": "multiple"}
    )
    def test_symbol_parameter_multiple(self, mock_request):
        # Provide multiple symbols and ensure URL is built correctly
        result = getEurostatData(symbol=["51640", "51641"])

        expected_url = (
            "https://api.tradingeconomics.com/eurostat/symbol/51640%2C51641?c=TESTKEY"
        )

        mock_request.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"symbol": "multiple"})
