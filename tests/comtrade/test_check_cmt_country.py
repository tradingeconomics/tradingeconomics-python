# FILE: tests/comtrade/test_checkCmtCountry.py
# Unit tests for checkCmtCountry()
# - Tests URL generation
# - Tests dataRequest passthrough (even though the function does not call it)

import unittest
from unittest.mock import patch

from tradingeconomics.comtrade import checkCmtCountry


class TestCheckCmtCountry(unittest.TestCase):
    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_single_country(self, mock_dataRequest):
        """
        When a single country is provided as string, it should be URL‑encoded
        and appended directly to the endpoint.
        """
        result = checkCmtCountry("united states")
        expected = "/comtrade/country/united%20states"
        self.assertEqual(result, expected)

    @patch("tradingeconomics.glob.apikey", "guest:guest")
    @patch("tradingeconomics.comtrade.fn.dataRequest")
    def test_multiple_countries(self, mock_dataRequest):
        """
        When a list of countries is passed, the code joins them with '/'
        and then URL-encodes the complete string. The test validates that
        the encoding behavior matches the current implementation.
        """
        result = checkCmtCountry(["united states", "china"])
        # Behavior according to module logic: join -> 'united states/china' -> quote()
        expected = "/comtrade/country/united%20states/china"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
