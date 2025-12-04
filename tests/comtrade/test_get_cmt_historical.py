# FILE: tests/comtrade/test_getCmtHistorical.py
# Unit tests for getCmtHistorical()
# - Tests URL generation
# - Tests error when symbol is missing
# - Tests passthrough of fn.dataRequest

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import getCmtHistorical


class TestGetCmtHistorical(unittest.TestCase):

    def test_no_symbol(self):
        """
        If symbol=None, the function must return the string:
        "A symbol is required!"
        (This function does NOT call dataRequest in this case.)
        """
        result = getCmtHistorical(symbol=None)
        self.assertEqual(result, "A symbol is required!")

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_symbol_basic(self, mock_dataRequest):
        """
        For a valid symbol, the module must generate:
        https://api.tradingeconomics.com/comtrade/historical/<encoded_symbol>
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtHistorical(symbol="PRTESP24031")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/historical/PRTESP24031"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_symbol_with_spaces(self, mock_dataRequest):
        """
        If symbol contains spaces, it must be URL-encoded.
        """
        mock_dataRequest.return_value = {"ok": True}

        result = getCmtHistorical(symbol="ABC 123")

        expected_url = (
            "https://api.tradingeconomics.com/comtrade/historical/ABC%20123"
        )

        mock_dataRequest.assert_called_once_with(api_request=expected_url, output_type=None)
        self.assertEqual(result, {"ok": True})


if __name__ == "__main__":
    unittest.main()